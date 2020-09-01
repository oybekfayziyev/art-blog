from django.urls import path
from .views import CommentView, add_comment

app_name = "comment"

urlpatterns = [
    path('<post>/', CommentView.as_view(), name='comment'),
    path('<post>/add-comment/', add_comment, name='add-comment')
]

