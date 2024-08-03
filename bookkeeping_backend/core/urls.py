# core/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MoneyAccountViewSet, UserViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'moneyaccounts', MoneyAccountViewSet)
router.register(r'users', UserViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]