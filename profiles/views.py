from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from project.utils.core import (get_object_by_username, 
                    get_count_object, 
                    get_all_objects, 
                    get_object_by_user,
                    is_blocked
                )
from django.contrib.auth import login, authenticate
from django.views import View
from profiles.models import Profile
from post.models import Post
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from follow.models import Follower, Following
from project.utils.utils import is_valid
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils import timezone
from allauth.account.views import LoginView, SignupView
from .forms import LoginForm, UserForm, ProfileForm
from follow.models import Blockuser

# Create your views here.

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
       
    def get(self, request, *args, **kwargs):

        context = {}

        profile, following, follower, block = self.get_queryset(request,*args, **kwargs)
        
        blocked = is_blocked(request.user.profile, block)
        
        if blocked:
       
            if profile is not None:     
                post = self.get_post(request).order_by('-id')
                
                following = self.get_following_count(profile)
                followers = self.get_follower_count(follower)
                context['profile'] = profile
                context['posts'] = post
                context['following'] = following
                context['followers'] = followers
                    
                return render(request, 'blog/profile.html', context)

            return HttpResponse('Profile not found 404 Error')
        
        return HttpResponse("You are blocked")
    
    def get_queryset(self, request, *args, **kwargs):
        username = self.kwargs.get('username')   
        profile = get_object_by_username(Profile, username = username)
       
        following = get_object_by_user(Following, profile)
        follower = get_object_by_user(Follower, profile)
        block = get_object_by_user(Blockuser, profile)
        
        return profile, following, follower, block
    
    def get_post(self, request):
        profile, _, _, _ = self.get_queryset(request)        
        post = Post.objects.filter(user = profile)

        return post
    
    def get_following_count(self, profile):
        
        count = get_count_object(Following, profile)
        print('count',count)
        return count
    
    def get_follower_count(self, follower):
        try:
            followers = follower.followers.count()
        except AttributeError:
            followers = 0
        return followers
    

class EditProfile(LoginRequiredMixin,View):

    def get_queryset(self, *args, **kwargs):
        
        username = self.kwargs.get('username')   
        profile = get_object_by_username(Profile, username = username)
       
        return profile, username
       
    def get(self, request, *args, **kwargs):

        profile, username = self.get_queryset(*args, **kwargs)   
        
        context = {}
       
        if request.user.username == username:
            if profile is not None:   
                context['profile'] = profile        

                return render(request, 'blog/edit_profile.html', context)
            
            return HttpResponse('User not Found 404 Error')
        
        return HttpResponse("You can not enter someone's profile settings!!!")
    
    def post(self, request, *args, **kwargs):

        profile, _ = self.get_queryset()
        
        default_image = profile.profile_pic
        current_username = profile.user.username
        form = self.get_all_forms(request,default_image)        
       
        all_profiles = get_all_objects(Profile)
        user = User.objects.get(username=profile.user.username)

        if is_valid(form, all_profiles, current_username):
             
            profile.profile_pic = form['profile_pic']                
            user.username = form['username']
            profile.first_name = form['fname']
            profile.last_name = form['lname']
            profile.bio = form['bio']
            if form['password']:
                user.set_password(form['password'])
            user.save()
            profile.save()
                       
            messages.info(request, 'Profile edited successfully')
            return redirect("/profile/{username}/".format(username= user.username))
        
        messages.info(request, 'Error occured while editing profile')
        return redirect("profile:edit-profile",username=user.username)
   

    def get_all_forms(self,request, default = None):
       
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        bio = request.POST['bio']
        profile_pic = request.FILES.get('photo',default)        
        password = request.POST["password"]
        confirm = request.POST['confirm']

        return {
                'fname':fname, 'lname':lname, 'username':username, 
                'email':email, 'bio':bio, 'profile_pic':profile_pic, 
                'password': password, 'confirm':confirm
            }
    
  
class MySignupView(View):    

    def get(self, request, *args, **kwargs):
        form = ProfileForm() 
        
        return render(request, "blog/signup.html", {
            'form' : form
        })

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST)
        
        if form.is_valid():
          
            form.save()
            username = form.cleaned_data.get('username')
            username_obj = User.objects.get(username=username)
            username = username_obj.username
            raw_password = username_obj.password
            first_name = username_obj.first_name
            last_name = username_obj.last_name

            user = authenticate(username=username, password=raw_password)
            profile = Profile(
                user = username_obj,
                first_name = first_name,
                last_name=last_name,
                created_date = timezone.now()
            )
            profile.save()
            login(request, username_obj)
            return redirect('/')

        else:         
            messages.info(request, "Error occured in signup page. ")
            form = ProfileForm()
        return render(request, 'blog/signup.html', {'form': form})        

    
   