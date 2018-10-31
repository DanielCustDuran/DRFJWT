from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from django.http import Http404
from .models import User
from .import serializers

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()
