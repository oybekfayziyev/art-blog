from django.db import models

# Create your models here.

from django.contrib.auth.models import User 
from project.utils.utils import upload_directory_path, generate_slug

from django.shortcuts import reverse


# Create your models here.


# TOKEN_GENERATOR_CLASS = get_token_generator()

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256) 
    bio = models.CharField(max_length=128, blank=True, null=True)   
    profile_pic = models.ImageField(upload_to= upload_directory_path, blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_date = models.DateTimeField(auto_now=True,blank=True,null=True)

    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse("profile:profile", kwargs={
            'username' : self.user.username
        })

    