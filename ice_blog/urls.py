from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

app_name = 'ice_blog'

router = SimpleRouter()
router.register('comments', views.CommentViewSet, basename='comments')
router.register('users', views.UserViewSet, basename='users')
router.register('posts', views.PostViewSet, basename='posts')

urlpatterns = router.urls