from django.shortcuts import render
from django.views.generic import ListView
from profiles.models import Profile
from post.models import Post
from project.utils.core import get_object_by_user, get_object_by_username, get_object_by_slug
from follow.models import Following
from follow.views import follow_unfollow_user
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from comment.views import add_comment
# Create your views here.

class HomeTemplateView(ListView):
    template_name = 'blog/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeTemplateView,self).get_context_data(*args, **kwargs)
        all_users, all_posts, profile = self.get_queryset()        
        following = get_object_by_user(Following, profile)
        
        context['all_users'] = all_users
        context['all_posts'] = all_posts
        context['following'] = following
                
        return context
    
    def get_queryset(self, *args, **kwargs):
        users = Profile.objects.all()
        post = Post.objects.all().order_by('-id')
        username = self.request.user.username
        profile = get_object_by_username(Profile, username)
      

        return users, post, profile
    
    def post(self, request, *args, **kwargs):
        description = request.POST.get('description')
        post = request.POST.get('post')        
           
        comment = add_comment(request.user.profile, post, description)

        return redirect("/")


@login_required
def follow_redirect_to_home(request, username,follow):
    follow_unfollow_user(request, username, follow)
    return redirect("/".format(username)) 

