from .permissions import IsAuthorOrReadOnly
from rest_framework import generics, permissions
from .models import Post, Comment
from .serializers import CommentSerializer, PostListSerializer, PostDetailSerializer

# Create your views here.

class PostList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly)
    lookup_field = 'id'
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

class CommentList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer