# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.http import HttpResponse
from django.urls import reverse_lazy

# Forms
from .forms import SignupForm

class LoginView(auth_views.LoginView):
    template_name = 'users/login.html'

class SignupView(FormView):
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data"""
        form.save()
        return super().form_valid(form)

class LogoutView(LoginRequiredMixin ,auth_views.LogoutView):
    pass