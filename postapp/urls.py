from django.urls import path
from .views import create_scheduled_post,show_published_posts

urlpatterns = [
    path('create/', create_scheduled_post, name='create_post'),
    path('post/', show_published_posts, name='show_post'),
]
