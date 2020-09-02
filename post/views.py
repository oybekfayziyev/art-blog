from django.shortcuts import render
from django.views import View
from project.utils.core import get_object_by_user, get_object_by_username
from profiles.models import Profile
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from .forms import PostForm
from django.contrib import messages

# Create your views here.

class PostView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        form = PostForm
        context = {
            'form' : form
        }
        return render(request, "blog/post.html", context=context)

    def post(self, request, *args, **kwargs):
        post = Post()
        # form = PostForm(request.POST, request.FILES)
        user = self.get_queryset(request)
        image = request.FILES.get('photo',)
        
        if image:
            image = 'post/{}/{}'.format(user, image) 
          
        description = request.POST.get('description')
        
        post.create(Post, user, image, description)  
        messages.info(request, 'Post added successfully')      
        return redirect("/")
    
    def get_queryset(self, request, *args, **kwargs):
         
        user = request.user.profile
        return user

        
        