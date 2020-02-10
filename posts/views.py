# Django
from django.views.generic import ListView
from django.shortcuts import render

class PostFeedView(ListView):
    template_name = 'posts/feed.html'