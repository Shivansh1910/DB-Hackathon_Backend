from django.shortcuts import render
from . import models, serializers
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view
# Create your views here.

# create a view for the database of user with the following fields


@api_view(['GET'])
def getUsers(request):
    users = models.User.objects.all()
    user_serializer = serializers.UserSerializer(users, many=True)
    return Response(user_serializer.data)

# get single user via email


@api_view(['POST'])
def getUser(request):
    reqData = request.data
    email = reqData['email']
    user = models.User.objects.get(email=email)
    user_serializer = serializers.UserSerializer(user, many=False)
    return Response(user_serializer.data)
