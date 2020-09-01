"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeTemplateView, follow_redirect_to_home
from profiles.views import MySignupView

urlpatterns = [
    path('', HomeTemplateView.as_view(),name='home'),
    path('<username>/follow/<follow>/redirect/', follow_redirect_to_home, name='follow-redirect'),
    path('admin/', admin.site.urls),
    path('post/', include('post.urls')),
    path('profile/', include('profiles.urls')),
    path('follow/',include('follow.urls')),
    path('comment/',include('comment.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/signup/user/', MySignupView.as_view(), name = 'account_signup_user')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
