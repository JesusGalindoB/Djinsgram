# Django
from django.db import models

# Models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(max_length=120)
    biography = models.TextField()
    phone_number = models.CharField(max_length=20, unique=True)

    picture = models.ImageField(
        upload_to='users/pictures', 
        blank=True, 
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
