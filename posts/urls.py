# Django 
from django.urls import path

# Views
from . import views

urlpatterns = [
    path(
        route='',
        view=views.PostFeedView.as_view(),
        name='feed'
    ),
]