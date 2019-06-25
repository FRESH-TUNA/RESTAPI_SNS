from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import *
from .CommentSerializer import CommentSerializer
from .UserSerializer import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    #read_only필드로 새로 추가할때는 적용 안함
    comments = CommentSerializer(read_only=True, source='comment_set', many=True)
    like_users = UserSerializer(read_only=True, source='like_user_set', many=True)
    
    # like_user_name_set = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    class Meta:
        model = Post
        exclude = ('user',)

    def create(self, validated_data):
        newPost = Post(
            user = validated_data['user'],
            title=validated_data['title'],
            content=validated_data['content'],
        )
        newPost.save()
        return newPost


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ('user','like_user_set')

    def create(self, validated_data):
        newPost = Post(
            user = validated_data['user'],
            title=validated_data['title'],
            content=validated_data['content'],
        )
        newPost.save()
        return newPost