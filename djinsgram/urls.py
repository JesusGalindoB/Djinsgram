# Django
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('', include(('posts.urls', 'posts'), namespace='posts')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('admin/', admin.site.urls),
]
