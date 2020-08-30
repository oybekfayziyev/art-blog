from django.shortcuts import render
from project.utils.core import get_object_by_username, get_object_by_user
from django.views import View
from profiles.models import Profile
from django.utils.decorators import method_decorator
from follow.models import Follower, Following
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required


class FollowersViews(LoginRequiredMixin, View):
    
    def get_queryset(self, *args, **kwargs):         
        username = self.kwargs.get('username')   
        
        profile = get_object_by_username(Profile, username)
       
        return profile

    def get(self, request, *args, **kwargs):
        context = {}
        username = self.kwargs.get('username')
        profile = self.get_queryset()
              
        follower = profile.followers.all()
        following = get_object_by_user(Following, profile)
        print('follower',follower)
        print('following', following)
        
        if follower:
            context['profile'] = profile
            context['following'] = following                      
            
            return render(request, 'blog/followers.html', context)
               
        return HttpResponse('You dont have followers')

class FollowingViews(LoginRequiredMixin, View):

    def get_queryset(self, *args, **kwargs):         
        username = self.kwargs.get('username')   
        
        profile = get_object_by_username(Profile, username)
       
        return profile

    def get(self, request, *args, **kwargs):
        context = {}
        username = self.kwargs.get('username')
        profile = self.get_queryset()
        
        print('profile',profile)
                
        following = get_object_by_user(Following, profile)
        print('following',following)
        
        if following:
            context['profile'] = profile
            context['following'] = following                      
            
            return render(request, 'blog/followings.html', context)        
       
        return HttpResponse('You dont have followings')

def follow_unfollow_followings(request, username, follow):

    following, _ = follow_unfollow_user(request, username, follow)
    return redirect("/follow/{}/followings/".format(username)) 

def follow_unfollow_followers(request, username, follow):
  
    _, followers = follow_unfollow_user(request, username, follow)
  
    return redirect("/follow/{}/followers/".format(username)) 

def follow_unfollow_user(request, username, follow):
    print('follow unfollow ',username)
    print(follow)
    follower, following, profile_following, profile_follower = get_object(username,follow)
    print('follower',follower)
    print('profile following',profile_following)
    print('following',following)
    if following:

        is_following_exist = is_following_user_exist(following.following.all(), follow)
        print('is exist',is_following_exist)
        if is_following_exist:
            following.remove(following, profile_follower)
        else:
            if not follower:
                print('not follower')
                Follower().create(Follower, profile_follower, profile_following)
            else:
                print('follower')
                follower.update(follower, profile_following)
            print('follower',follower)
            following.update(following, profile_follower)                
    else:
        profile_follow, profile = get_queryset(username, follow)
        Following().create(Following, profile, profile_follow)
        if follower:
            follower.update(follower, following)
        else:
            Follower().create(Follower, profile_follow, profile)

    return following, follower

def is_following_user_exist(following_user, user):
    for following in following_user:       
        if following.user.username==user:
            return True
    
    return False


def get_queryset(username, follow):
    profile = get_object_by_username(Profile, username)
  
    profile_follow = get_object_by_username(Profile, follow)  
    
    return profile_follow, profile

def get_object(username,follow): 
    profile_follower, profile_following = get_queryset(username, follow)
    _follow = get_object_by_user(Following, profile_following)
     
    follower = get_object_by_user(Follower, profile_follower)
   
    return follower, _follow, profile_following, profile_follower
