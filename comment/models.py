from django.db import models
from profiles.models import Profile
from post.models import Post 
# Create your models here.

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comment')
    comment = models.CharField(max_length=512)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username