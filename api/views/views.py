from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api.serializers.PostSerializer import PostSerializer, PostListSerializer
from api.serializers.CommentSerializer import CommentSerializer
from api.models import *
from django.contrib.auth.models import User
import logging

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    # def list(self, request):
    #     pass

    def create(self, request):
        serializer = PostSerializer(data=request.data)
        
        if serializer.is_valid():
            # logging.error(serializer.validated_data)
            newPost = serializer.save(user = User.objects.get(username='rose'))
            # if request.user.is_authenticated:
                # newNews.user = User.objects.get(username='rose')
                # newNews.user = request.user
                # newNews.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk, format=None):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post)
        # if serializer.is_valid():
            # logging.error(serializer.validated_data)
            # newPost = serializer.save(user = User.objects.get(username='rose'))
            # if request.user.is_authenticated:
                # newNews.user = User.objects.get(username='rose')
                # newNews.user = request.user
                # newNews.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass

    @action(detail=True, methods=['post'])
    def likeOnPost(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        #get_or_object의 반환타입은 tuple (object ,만들어졌으면 true 반환)
        post_like, post_like_created = post.like_set.get_or_create(user = User.objects.get(username='rose'))

        if not post_like_created:
            post_like.delete()
            return Response({'like':'disabled'}, status=status.HTTP_200_OK)
        else:
            return Response({'like':'abled'}, status=status.HTTP_200_OK)
    

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    # def list(self, request):
    #     pass

    def create(self, request):
        serializer = CommentSerializer(data=request.data)
        
        if serializer.is_valid():
            # logging.error(serializer.validated_data)
            newComment = serializer.save(
                user = User.objects.get(username='rose'), 
                post = Post.objects.get(pk=request.GET.get('post'))
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class LikeViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     # permission_classes = (IsAuthenticatedOrReadOnly,)
    # def list(self, request):
    #     pass

#     def create(self, request):
#         serializer = CommentSerializer(data=request.data)
        
#         if serializer.is_valid():
#             # logging.error(serializer.validated_data)
#              = serializer.save(
#                 user = User.objects.get(username='rose'), 
#                 post = Post.objects.get(pk=request.GET.get('post'))
#             )
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# post = get_object_or_404(Post, pk=post_id)
    
#     #get_or_object의 반환타입은 tuple (object ,만들어졌으면 true 반환)
#     post_like, post_like_created = post.like_set.get_or_create(user = request.user)

#     if not post_like_created:
#         post_like.delete()
#         return redirect('/testRead/' + str(post.id))
#     return redirect('/testRead/' + str(post.id))