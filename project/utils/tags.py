from django import template
from comment.models import Comment
from project.utils.core import get_object_by_slug, get_object_by_user, get_object_by_username
from post.models import Post
from profiles.models import Profile
from follow.models import Follower

register = template.Library()

@register.filter
def is_equal(value1, value2):
   
    if value1 == value2:
        
        return True
    
    return False

@register.filter
def get_comment_total(slug):
    post = get_object_by_slug(Post, slug=slug)
    comment = Comment.objects.filter(post = post)

    return comment.count()

@register.filter
def get_follower_total(profile):
    profile = get_object_by_username(Profile, username=profile)
    follower = get_object_by_user(Follower, user = profile)

    try:
        count = follower.followers.count()
    except AttributeError:
        count = 0
    
    return count
