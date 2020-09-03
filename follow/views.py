from django.shortcuts import render
from project.utils.core import get_object_by_username, get_object_by_user,is_blocked
from django.views import View
from profiles.models import Profile
from django.utils.decorators import method_decorator
from follow.models import Follower, Following, Blockuser
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
        follower = get_object_by_user(Follower, profile)
        block = get_object_by_user(Blockuser, profile)
        return profile, follower, block

    def get(self, request, *args, **kwargs):
        context = {}
        
        profile, followers, block = self.get_queryset()        
        following = get_object_by_user(Following, request.user.profile)
       
        if followers:
            context['profile'] = profile
            context['following'] = following  
            context['followers'] = followers 
            context['blockusers'] = block                     
            
            return render(request, 'blog/followers.html', context)
               
        return HttpResponse('You dont have followers')

class FollowingViews(LoginRequiredMixin, View):

    def get_queryset(self, *args, **kwargs):         
        username = self.kwargs.get('username')
             
        profile = get_object_by_username(Profile, username)
        block = get_object_by_user(Blockuser, profile)

        return profile, block

    def get(self, request, *args, **kwargs):
        context = {}
        username = self.kwargs.get('username')
        profile, block = self.get_queryset()
        blocked = is_blocked(request.user.profile, block)

        if blocked:
            following = get_object_by_user(Following, profile)
            if following:
                context['profile'] = profile
                context['following'] = following  
                context['blockusers'] = block                   
                
                return render(request, 'blog/followings.html', context) 

            return HttpResponse('You dont have followings')
        return HttpResponse("You can not enter this profile. You are blocked")       
       
        

def follow_unfollow_followings(request, username, follow):
    
    following, _ = follow_unfollow_user(request, username, follow)
    return redirect("/follow/{}/followings/".format(username)) 

def follow_unfollow_followers(request, username, follow):
  
    _, followers = follow_unfollow_user(request, username, follow)
  
    return redirect("/follow/{}/followers/".format(username)) 

@login_required
def follow_unfollow_user(request, username, follow):
    
    follower, following, profile_following, profile_follower = get_object(username,follow)
   
    if following:

        is_following_exist = is_following_user_exist(following.following.all(), follow)
        
        if is_following_exist:
            following.remove(following, profile_follower)
            follower.remove(follower, profile_following)
        else:
            if not follower:
                 
                Follower().create(Follower, profile_follower, profile_following)
            else:
                
                follower.update(follower, profile_following)
           
            following.update(following, profile_follower)                
    else:
        profile_follow, profile = get_queryset(username, follow)
        Following().create(Following, profile, profile_follow)
        print('follower',follower)
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

@login_required
def block_unlock_user(request, block_user):

    user = request.user.profile
    block_user = get_object_by_username(Profile, block_user)
    print('user',user)
    block_user_obj = get_object_by_user(Blockuser, user = user)
    print('block user obj', block_user_obj)
    if block_user_obj:
        
        if block_user in block_user_obj.blocked.all():
            print('remove')
            block_user_obj.remove(block_user_obj, block_user)
        else:
            print('update')
            block_user_obj.update(block_user_obj, block_user)

    else:
        Blockuser().create(Blockuser, user, block_user)


    return HttpResponse("Success")