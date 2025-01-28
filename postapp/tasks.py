from celery import shared_task
from .models import Post
from django.utils import timezone



@shared_task
def publish_post(post_id):
    post = Post.objects.get(id=post_id)
    
    if timezone.now() >= post.publish_date:
        post.status = 'published'
        post.save()
        
        
        print(f"Post {post.id} published successfully")
    else:
        print(f"Post {post.id} scheduled for publication at {post.publish_date}")
