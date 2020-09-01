from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from project.utils.core import get_object_by_username, get_count_object, get_all_objects, get_object_by_user
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

# Create your views here.

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
       

    def get(self, request, *args, **kwargs):

        context = {}

        profile, following, follower = self.get_queryset(*args, **kwargs)   
        if profile is not None:     
            post = self.get_post()
            print('profile',profile)
            following = self.get_following_count(profile)
            print('profile following',following)
            context['profile'] = profile
            context['posts'] = post
            context['following'] = following
                

            return render(request, 'blog/profile.html', context)

        return HttpResponse('Profile not found 404 Error')
    
    def get_queryset(self, *args, **kwargs):
        username = self.kwargs.get('username')   
        profile = get_object_by_username(Profile, username = username)
        following = get_object_by_user(Following, profile)
        follower = get_object_by_user(Follower, profile)
        
        return profile, following, follower
    
    def get_post(self):
        profile, _, _ = self.get_queryset()        
        post = Post.objects.filter(user = profile)

        return post
    
    def get_following_count(self, profile):
        
        count = get_count_object(Following, profile)
        return count
    

class EditProfile(LoginRequiredMixin,View):

    def get_queryset(self, *args, **kwargs):
        
        username = self.kwargs.get('username')   
        profile = get_object_by_username(Profile, username = username)
       
        return profile
       
    def get(self, request, *args, **kwargs):

        profile = self.get_queryset(*args, **kwargs)   
        
        context = {}
       
         
        if profile is not None:   
            context['profile'] = profile        

            return render(request, 'blog/edit_profile.html', context)
        
        return HttpResponse('User not Found 404 Error')
    
    def post(self, request, *args, **kwargs):

        profile = self.get_queryset()
        
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
    


class MyLoginView(LoginView):
    

    def get_context_data(self, **kwargs):           
        context = super(MyLoginView, self).get_context_data(**kwargs)
        context['form'] = LoginForm() # add form to context
        
        print(context)
        return context
    
    # def form_valid(self, form):
    #     # By assigning the User to a property on the view, we allow subclasses
    #     # of SignupView to access the newly created User instance
    #     print('retaurant',self.restaurant_form)   
    #     print('retaurant',form)   
    #     self.restaurant_form = form.save(self.request)   
    #     print('retaurant',self.restaurant_form)      
    #     return complete_signup(
    #         self.request, self.user,
    #         app_settings.EMAIL_VERIFICATION,
    #         self.get_success_url())
    
class MySignupView(SignupView):    

    def get_context_data(self, **kwargs):           
        context = super(MySignupView, self).get_context_data(**kwargs)
         
        context['form'] = UserForm() # add form to context
        context['profile_form'] = ProfileForm()

        print('kwargs')
        print(' dxxxx',context)
        return context
    
    def form_valid(self, form, profile_form):
        # By assigning the User to a property on the view, we allow subclasses
        # of SignupView to access the newly created User instance
        self.user = form.save(self.request)

        print('form')
        print('profile form')


        try:
            return complete_signup(
                self.request, self.user,
                app_settings.EMAIL_VERIFICATION,
                self.get_success_url())
        except ImmediateHttpResponse as e:
            return e.response

   