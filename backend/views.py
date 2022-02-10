from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .models import MetaUser
from .serializers import MetaUserSerializer, UserSerializer

#



class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]




class MetaUserViewSet(viewsets.ModelViewSet):

    queryset = MetaUser.objects.all()
    serializer_class = MetaUserSerializer
    permission_classes = [permissions.IsAuthenticated]


# Create your views here.
