# core/serializers.py
from rest_framework import serializers
from .models import MoneyAccount, User, Transaction

class MoneyAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoneyAccount
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'