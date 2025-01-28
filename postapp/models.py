from django.db import models
from django.utils import timezone



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    publish_date = models.DateTimeField(null=True, blank=True)  #publish_date
    status = models.CharField(max_length=10, choices=[
        ('draft', 'Draft'),
        ('scheduled', 'Scheduled'),
        ('published', 'Published')
    ], default='draft')

    def __str__(self):
        return self.title

    @property
    def is_published(self):
        return self.status == 'published'

    def schedule_for_publish(self):
        if self.publish_date and self.is_future():
            self.status = 'scheduled'
            self.save()

    def publish(self):
        if self.publish_date and self.is_future():
            current_time = timezone.now()
            if current_time >= self.publish_date:
                self.status = 'published'
                self.save()
                # Add any additional logic here for publishing actions
                print(f"Post {self.id} published successfully")
            else:
                print(f"Post {self.id} is not yet scheduled for publication")

    def is_future(self):
        return timezone.now() < self.publish_date
