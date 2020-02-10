# Django 
from django import forms

# Models
from django.contrib.auth.models import User
from .models import Profile

class SignupForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=50)

    password = forms.CharField(
        max_length=70, 
        widget=forms.PasswordInput()
    )
    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)
    email = forms.EmailField(min_length=6, max_length=70)

    def clean_username(self):
        """Verify that the user name is unique"""
        data = self.cleaned_data['username']
        username_taken = User.objects.filter(username=data).exists()

        if username_taken:
            raise forms.ValidationError("Username already exists")
        return data

    def clean(self):
        """Check for password matching"""
        data = super().clean()
        password = data['password']
        password_confirmation = data["password_confirmation"]

        if password != password_confirmation:
            raise forms.ValidationError('password do not match.')

        return data

    def save(self):
        """Create user and profile"""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile.objects.create(user=user)

