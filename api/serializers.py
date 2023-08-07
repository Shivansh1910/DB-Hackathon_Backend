from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'

class SecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Security
        fields = '__all__'