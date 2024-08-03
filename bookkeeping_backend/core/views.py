# core/views.py
from rest_framework import viewsets
from .models import MoneyAccount, User, Transaction
from .serializers import MoneyAccountSerializer, UserSerializer, TransactionSerializer

class MoneyAccountViewSet(viewsets.ModelViewSet):
    queryset = MoneyAccount.objects.all()
    serializer_class = MoneyAccountSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer