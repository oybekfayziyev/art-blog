from django.shortcuts import render
from django.views import View
from project.utils.core import get_object_by_user, get_object_by_slug, get_object_by_post
from profiles.models import Profile
from post.models import Post
from .models import Comment
from django.utils import timezone
from django.shortcuts import redirect

# Create your views here.

class CommentView(View):

    def get(self, request, *args, **kwargs):
        context = {}
        comment, post = self.get_queryset(*args, **kwargs)
       
        context['comments'] = comment
        context['post'] = post
        return render(request, 'blog/comment.html', context=context)

    def get_queryset(self, *args, **kwargs):
        slug = self.kwargs.get('post') 
        post = get_object_by_slug(Post, slug=slug)        
        comment = Comment.objects.filter(post=post).order_by('-id')
       
        return comment, post
    
    def post(self, request, *args, **kwargs):
        description = request.POST.get('description')
        post = request.POST.get('post')        
        print('DESCRIPTION', description)
        print('P',post)

        comment = add_comment(request.user.profile, post, description)

        return redirect("/comment/{}/".format(post))

def add_comment(user, post, comment):
    post = get_object_by_slug(Post, slug=post)    
    Comment().create(Comment, post, user, comment)

    return redirect("/")
    
def is_valid(comment):
    if comment:
        return True
    return False
