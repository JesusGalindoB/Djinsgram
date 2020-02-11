# Django
from django.views.generic import ListView
from django.shortcuts import render

# Models
from .models import Post

class PostFeedView(ListView):
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    context_object_name = 'posts'