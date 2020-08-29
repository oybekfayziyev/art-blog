from django.urls import path
from .views import ProfileView, EditProfile


app_name = "profile"

urlpatterns = [
    path('<username>/', ProfileView.as_view(), name='profile'),
    path('<username>/edit/', EditProfile.as_view(), name='edit-profile'),    
]

