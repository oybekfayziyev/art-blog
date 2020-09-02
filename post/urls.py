from django.urls import path
from .views import PostView

app_name = "post"

urlpatterns = [
    path('', PostView.as_view(), name='post'),
    # path('<post>/add-comment/', add_comment, name='add-post')
]

