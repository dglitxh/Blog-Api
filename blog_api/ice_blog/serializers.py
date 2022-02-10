
from rest_framework import serializers
from .models import Post, Comment

class PostListSerializer(serializers.ModelSerializer):
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

class PostDetailSerializer(serializers.ModelSerializer):
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
            'active'

        ]