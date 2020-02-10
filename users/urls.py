# Django
from django.urls import path

# Views
from . import views

urlpatterns = [
    path(
        route='login/', 
        view=views.LoginView.as_view(),
        name='login'
    ),
    path(
        route='signup/',
        view=views.SignupView.as_view(),
        name='signup'
    ),
]