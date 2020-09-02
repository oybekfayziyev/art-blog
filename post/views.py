from django.shortcuts import render
from django.views import View
from project.utils.core import get_object_by_user, get_object_by_username
from profiles.models import Profile
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from .forms import PostForm
from django.contrib import messages
from django.utils import timezone
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
        form = PostForm(request.POST, request.FILES)
        print('form',form)
        if form.is_valid():
            print('valid true')
            # image = request.FILES.get('photo',)
            image = form.cleaned_data.get('image')
            user = self.get_queryset(request)
            description = form.cleaned_data.get('description')
            post = Post(
                user = user,
                image = image,
                description = description,
                created_date = timezone.now()
            )
            post.save()
             
       
        messages.info(request, 'Post added successfully')      
        return redirect("/")
    
    def get_queryset(self, request, *args, **kwargs):
         
        user = request.user.profile
        return user

        
        