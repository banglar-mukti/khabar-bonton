from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer

# Create your views here.

class UserViewset(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

