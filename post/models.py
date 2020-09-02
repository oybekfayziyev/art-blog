from django.db import models
from django.contrib.auth.models import User 
from profiles.models import Profile
from django.shortcuts import reverse
from project.utils.utils import upload_directory_path, generate_slug
from django.utils import timezone
from django.db.models.signals import pre_save
from PIL import Image
# Create your models here.

class PostExtraImage(models.Model):
	title = models.CharField(max_length = 64, null=True,blank=True)
	image = models.ImageField(upload_to = upload_directory_path)
	post = models.ForeignKey('Post', null=True,blank=True, on_delete=models.CASCADE, related_name='images')

	class Meta:
		verbose_name_plural = 'Images'
                    
class Post(models.Model):

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name = 'post')
    image = models.ImageField(upload_to=upload_directory_path, blank=True, null=True)
    content = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(max_length=512,blank=True,null=True)
    slug = models.SlugField(unique=True, default = generate_slug, blank=True,null=True)
    caption = models.CharField(max_length=512,blank=True,null=True)
    image_likes = models.ManyToManyField(Profile, related_name='likes',blank=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True,null=True)
    update_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.slug
    
    def get_absolut_url(self):
        return reverse("profile:user", kwargs={
            'username' : self.user.username
        })
    
    def create(self, instance, user, photo, description):
        
        obj = instance.objects.create(
            user = user,   
            image = photo,                         
            description = description,
            created_date = timezone.now()
        )

        # if photo:            
        #     photo = upload_directory_path(obj, photo) 
        #     print('PHOTO', photo)
        #     obj.image = photo
        #     obj.save()
            
        #     f = file()
            
                    
        # obj.image = ImageFile(photo)
        # obj.save()

       

  

