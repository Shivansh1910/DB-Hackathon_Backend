from rest_framework import serializers
from . import models


class DBUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DBUser
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ('id', 'name')


class UserBookSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = models.UserBook
        fields = '__all__'


class CounterPartySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CounterParty
        fields = '__all__'


class SecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Security
        fields = '__all__'


class TradeSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    counterparty = CounterPartySerializer()
    security = SecuritySerializer()

    class Meta:
        model = models.Trade
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notification
        fields = '__all__'
