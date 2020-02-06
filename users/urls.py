# Django
from django.urls import path

# Views
from . import Views

urlpatterns = [
    path(
        route='login', 
        view=views.login,
        name='name'
    ),
]