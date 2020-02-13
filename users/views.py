# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, UpdateView, DetailView
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Forms
from .forms import SignupForm

# Models
from .models import Profile
from django.contrib.auth.models import User
from posts.models import Post

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
        
class UpdateProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self):
        """Return user's profile"""
        return self.request.user.profile

    def get_success_url(self):
        """Return to user's profile"""
        username = self.object.user.username
        return reverse('posts:feed')

class UserDetailView(LoginRequiredMixin, DetailView):
    template_name = 'users/detail.html'
    queryset = User.objects.all()
    slug_field = 'username'
    slug_url_kwarg = 'username'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user's posts to context"""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context 

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    pass