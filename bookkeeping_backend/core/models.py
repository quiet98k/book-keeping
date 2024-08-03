from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

# Create your models here.
class MoneyAccount(models.Model):
    name = models.CharField(max_length=255)  # e.g., 'Cash', 'Savings Account'
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    currency = models.CharField(max_length=10, default='USD')
    
    def __str__(self):
        return f'{self.name} - {self.balance} {self.currency}'
    
    def update_balance(self, amount):
        """Updates the balance of the account."""
        self.balance += amount
        if self.balance < 0:
            raise ValidationError('Insufficient funds.')
        self.save()

    def validate_currency(self, currency):
        """Validate if the currency matches."""
        if self.currency != currency:
            raise ValidationError('Currency mismatch.')

class User(AbstractUser):
    # Add any additional fields here if needed
    money_accounts = models.ManyToManyField(MoneyAccount, related_name='users')

    def __str__(self):
        return self.username
    
class Transaction(models.Model):
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Use positive values for deposits and negative for withdrawals
    date = models.DateField()
    category = models.CharField(max_length=100, blank=True, null=True)
    currency = models.CharField(max_length=10, default='USD')
    account = models.ForeignKey(MoneyAccount, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def clean(self):
        if self.amount == 0:
            raise ValidationError('Transaction amount cannot be zero.')
        if self.account.currency != self.currency:
            raise ValidationError('Transaction currency must match account currency.')

    def __str__(self):
        return f'{self.description} - {self.amount} {self.currency} on {self.date}'
    

