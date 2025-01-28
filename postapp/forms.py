from django import forms
from .models import Post




class PublishForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'publish_date']
        widgets = {
            'publish_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
