from django.db import models
from profiles.models import Profile
from django.contrib.auth.models import User 
from django.utils import timezone
# Create your models here.

class Follower(models.Model):
    
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, unique=True)
    followers = models.ManyToManyField(Profile, related_name='followers')
    accepted = models.BooleanField(default = False)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def update(self, instance, follower):
      
        instance.updated_date = timezone.now()
        instance.followers.add(follower)        
        instance.save()

        return instance

    def create(self, instance, user, follower):
       
        follower_obj = instance.objects.create(
            user = user,
            created_date = timezone.now()
        )
        follower_obj.followers.add(follower)
        follower_obj.save()

    def remove(self, instance,follower):
        instance.updated_date = timezone.now()
        instance.followers.remove(follower)        
        instance.save()

        return instance
        
    def __str__(self):
        return self.user.user.username

class Following(models.Model):

    user = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='following_user')
    following = models.ManyToManyField(Profile, related_name='following')

    created_date = models.DateTimeField(auto_now_add=True, blank=True,null=True)
    updated_date = models.DateTimeField(auto_now = True, blank=True,null=True)

    def __str__(self):
        return self.user.user.username

    def update(self,instance,follower):
        
        instance.updated_date = timezone.now()
        instance.following.add(follower)     
        instance.save()
       
        return instance

    def create(self,instance,user,follower):
        
        follower_obj = instance.objects.create(
            user = user,
            created_date = timezone.now()
        )        
       
        follower_obj.following.add(follower)        
        return follower_obj

    def remove(self, instance,follower):
    
        instance.following.remove(follower)        
        instance.save()

        if not instance.following.all():
            instance.delete()
      
        return instance