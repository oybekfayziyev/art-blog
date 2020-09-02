from django.urls import path
from .views import ( FollowingViews, 
            follow_unfollow_user,FollowersViews, 
            follow_unfollow_followings,
            follow_unfollow_followers,
            block_unlock_user
        )

app_name = "follow"

urlpatterns = [
    path('<username>/followings/', FollowingViews.as_view(), name='followings'), 
    path('<username>/followers/', FollowersViews.as_view(), name='followers'),   
    path('<username>/follow/<follow>/', follow_unfollow_followings, name='follow_to'),
    path('<username>/follower/<follow>/', follow_unfollow_followers, name='follower_to'),
    path('block/<block_user>/', block_unlock_user, name='block'),
]

