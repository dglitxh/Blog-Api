from django.urls import path
from . import views

app_name = 'ice_blog'

urlpatterns = [
    path('posts', views.PostList.as_view(), name='posts'),
    path('posts/<int:id>', views.PostDetail.as_view(), name='post_detail'),
    path('comments/', views.CommentList.as_view(), name='comments'),
]