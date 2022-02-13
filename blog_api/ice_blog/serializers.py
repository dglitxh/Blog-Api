from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'body',
            'author',
            'post_category',
            'thumbnail',
            'status'
        ]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'post',
            'name',
            'body',
         
            
        ]

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
    class Meta:
        model = User
        fields = [
           'id',
           'username',
           'posts',
        ]