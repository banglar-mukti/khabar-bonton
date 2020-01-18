from rest_framework import generics
from .models import CustomUser, Post
from .serializers import UserSerializer, PostSerializer

# Create your views here.


class UserViewset(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()


class PostViewset(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()