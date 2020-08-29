from django.urls import path
from .views import FollowersView, follow_unfollow_user

app_name = "follow"

urlpatterns = [
    path('<username>/followers/', FollowersView.as_view(), name='followers'),   
    path('<username>/follow/<follow>/', follow_unfollow_user, name='follow_to'),
]

