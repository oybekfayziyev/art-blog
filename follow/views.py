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



class FollowersView(LoginRequiredMixin, View):

    def get_queryset(self, *args, **kwargs):         
        username = self.kwargs.get('username')   
        print('username',username)
        profile = get_object_by_username(Profile, username)
        print('profile',profile.followers.all())
       
        return profile

    def get(self, request, *args, **kwargs):
        context = {}
        username = self.kwargs.get('username')
        profile = self.get_queryset()
              
        followers = profile.followers.all()
        following = get_object_by_user(Following, profile)
        print('followers',followers)
        print('following', following)
        if followers:
            context['profile'] = profile
            context['following'] = following 
            context['followers'] = followers           
            
            return render(request, 'blog/followings.html', context)
        
       
        return HttpResponse('You dont have followers')

def follow_unfollow_user(request, username, follow):
    
    follower, following, profile_following = get_object(username,follow)
    print('follower',follower)
    print('following',following)
    if following:
        for follow_to in following.following.all():
            print('follow_to', follow_to)
            if follow_to.user.username != follow:
                if not follower:
                    follower = Follower().create(Follower, follow_to.user.profile, profile_following)
                else:
                    follower = follower.update(follower, profile_following)
                print('follower',follower)
                following.update(following, follower)
                print('yes')
                print('followerssssss',follower)                   
            
            else:
                print('noooo')
                following.remove(following, follow_to)
                
    else:
        profile_follow, profile = get_queryset(username, follow)
        Following().create(Following, profile, profile_follow)
        if follower:
            follower.update(follower, following)
        else:
            Follower().create(Follower, profile_follow, profile)

    return HttpResponse('Yeees')

    
    
    return HttpResponse('User not found')


def get_queryset(username, follow):
    profile = get_object_by_username(Profile, username)
    print('profile',profile)
    profile_follow = get_object_by_username(Profile, follow)  
    print('profile follow',profile_follow)

    return profile_follow, profile

def get_object(username,follow): 
    profile_follower, profile_following = get_queryset(username, follow)
    _follow = get_object_by_user(Following, profile_following)
    print('follow',_follow)
    follower = get_object_by_user(Follower, profile_follower)
    print('finished', follower)
    return follower, _follow, profile_following
