from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics, permissions, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serialzers import PostSerializer
from user.models import CustomUser, Profile
from ..models import Post
# Create your views here.

class Posts(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        posts = Post.objects.all()
        serializers = PostSerializer(posts, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    def post(self, request, *args, **kwargs):
        user_profile = request.user.profile.get()

        if not user_profile:
            return Response({"error": "User profile not found"}, status=status.HTTP_400_BAD_REQUEST)

        mutable_data = request.data.copy()
        mutable_data['profile'] = user_profile.pk

        # Assuming you have a PostSerializer defined
        serializer = PostSerializer(data=mutable_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class AccessPost(APIView):

    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def get(self,request,id):
        post = get_object_or_404(Post, id=id)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request,id):
        post = get_object_or_404(Post, id=id)
        post_serializer = PostSerializer(post, data=request.data)

        if post_serializer.is_valid():
            post = post_serializer.save()
            return Response({"message":"update successful"}, status=status.HTTP_202_ACCEPTED)
        return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,id):
        post = Post.objects.get(id=id)
        post.delete()
        return Response({"message":"delete successful"}, status=status.HTTP_202_ACCEPTED)
    

class FollowFeed(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        profile = user.profile.first()

        following=profile.followers.all()
        feed=[]
        for prof in following:
            feed.extend(prof.post_set.all())

        feed.sort
        serialized_feed=[]

