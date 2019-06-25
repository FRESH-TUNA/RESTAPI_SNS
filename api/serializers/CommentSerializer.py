from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import *


class CommentSerializer(serializers.ModelSerializer):
    #read_only필드로 새로 추가할때는 적용 안함
    # like_user_name_set = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    class Meta:
        model = Comment
        exclude = ('user','post')

    def create(self, validated_data):
        newComment = Comment(
            user = validated_data['user'],
            post = validated_data['post'],
            content = validated_data['content'],
        )
        newComment.save()
        return newComment
