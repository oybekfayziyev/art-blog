from django.db import models
from profiles.models import Profile
from post.models import Post 
from django.utils import timezone
# Create your models here.

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comment')
    comment = models.CharField(max_length=512)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post.slug
    
    def create(self, instance, post, user, comment):
        instance.objects.create(
            post = post,
            user = user,            
            comment = comment,
            created_date = timezone.now()
        )
 