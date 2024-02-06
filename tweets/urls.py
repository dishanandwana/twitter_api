from django.urls import path
from .views import CreateUserAPIView, CreateTweetAPIView, GetUserFeedAPIView

urlpatterns = [
    path('user/', CreateUserAPIView.as_view(), name='create_user'),
    path('tweet/', CreateTweetAPIView.as_view(), name='create_tweet'),
    path('user/<uuid:id>/feed/', GetUserFeedAPIView.as_view(), name='get_user_feed'),
]
