from django.shortcuts import render
from django.views.generic import ListView
from profiles.models import Profile
from post.models import Post
# Create your views here.

class HomeTemplateView(ListView):
    template_name = 'blog/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeTemplateView,self).get_context_data(*args, **kwargs)
        all_users, all_posts = self.get_queryset()
        print('all posts',all_posts)
        print('all users', all_users)
        context['all_users'] = all_users
        context['all_posts'] = all_posts

        return context
    
    def get_queryset(self, *args, **kwargs):
        profile = Profile.objects.all()
        post = Post.objects.all().order_by('-id')

        return profile, post
    


