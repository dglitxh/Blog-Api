from cgitb import lookup
from django.shortcuts import render
from rest_framework import generics
from .models import Post, Comment
from .serializers import PostListSerializer, PostDetailSerializer

# Create your views here.

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

