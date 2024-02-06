from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import User, Tweet
from .serializers import UserSerializer, TweetSerializer

class CreateUserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreateTweetAPIView(generics.CreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

class GetUserFeedAPIView(generics.ListAPIView):
    serializer_class = TweetSerializer

    def get_queryset(self):
        user_id = self.kwargs['id']
        return Tweet.objects.filter(user__id=user_id)
