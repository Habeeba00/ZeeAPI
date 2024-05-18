from django.contrib.auth.models import User
from .Serializers import UserSerializer
from rest_framework import viewsets
from .models import Profile

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer