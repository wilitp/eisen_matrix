from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
