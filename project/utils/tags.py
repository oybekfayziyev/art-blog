from django import template
from comment.models import Comment
from project.utils.core import get_object_by_slug, get_object_by_user
from post.models import Post

register = template.Library()

@register.filter
def is_equal(value1, value2):
    print('value1',value1)
    print('value2', value2)
    print(type(value1))
    print(type(value2))
    if value1 == value2:
        print('yes')
        return True
    
    return False

@register.filter
def get_comment_total(slug):
    post = get_object_by_slug(Post, slug=slug)
    comment = Comment.objects.filter(post = post)

    return comment.count()