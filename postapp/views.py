from django.shortcuts import render, redirect
from .models import Post
from .tasks import publish_post
from .forms import PublishForm
from django.utils import timezone
from datetime import datetime
from celery.exceptions import SoftTimeLimitExceeded, TimeoutError
# from celery.schedules import crontab



def show_published_posts(request):
    posts = Post.objects.filter(status='published').order_by('-publish_date')
    return render(request, 'display_post.html', {'posts': posts})




def create_scheduled_post(request):
    if request.method == 'POST':
        form = PublishForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            
            publish_date_str = form.cleaned_data['publish_date']
            print(f"Received publish date: {publish_date_str}")
            
            if isinstance(publish_date_str, datetime):
                publish_date = publish_date_str
            else:
                # If it's a string, parse it
                publish_date = timezone.make_aware(datetime.strptime(publish_date_str, '%Y-%m-%dT%H:%M'))
            
            # Get the current time
            current_time = timezone.now()
            print(f"Current time: {current_time}")
            
            # If the publish date is in the past, set it to the next occurrence
            if publish_date <= current_time:
                publish_date = publish_date.replace(year=current_time.year, month=current_time.month, day=current_time.day)
                publish_date += timezone.timedelta(days=1)
            
            print(f"Adjusted publish date: {publish_date}")
            
            post.publish_date = publish_date
            post.schedule_for_publish()
            post.save()
            
            try:
                # Schedule the task to run at the calculated publish_date
                publish_post.apply_async((post.id,), eta=publish_date)
                print(f"Task scheduled for: {publish_date}")
                
                # Redirect to home page after scheduling
                return redirect('create_post')
            
            except SoftTimeLimitExceeded:
                print("Task exceeded time limit")
            except TimeoutError:
                print("Task timed out")
            except Exception as e:
                print(f"An error occurred: {str(e)}")
        else:
            print(form.errors)
    
    form = PublishForm()
    posts = Post.objects.filter(status='published').order_by('-publish_date')
    return render(request, 'create_post.html', {'form': form, "posts": posts})
