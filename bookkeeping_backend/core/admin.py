from django.contrib import admin
from .models import MoneyAccount, User, Transaction

# Register your models here.
@admin.register(MoneyAccount)
class MoneyAccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'currency')
    search_fields = ('name', 'currency')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('description', 'amount', 'date', 'category', 'currency', 'account', 'user')
    search_fields = ('description', 'category', 'currency')
    list_filter = ('date', 'category', 'currency', 'account', 'user')