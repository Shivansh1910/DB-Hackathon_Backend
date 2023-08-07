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

@api_view(['GET'])
def getSecurities(request):
    securities = models.Security.objects.all()
    security_serializer = serializers.SecuritySerializer(securities, many=True)
    return Response(security_serializer.data)

# get security by isin
@api_view(['POST'])
def getSecurity(request):
    reqData = request.data
    id = reqData['isin']
    security = models.Security.objects.get(isin=isin)
    security_serializer = serializers.SecuritySerializer(security, many=False)
    return Response(security_serializer.data)