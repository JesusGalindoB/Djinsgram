# Django
from django.urls import path

# Views
from . import views

urlpatterns = [
    path(
        route='login/', 
        view=views.login,
        name='name'
    ),
]