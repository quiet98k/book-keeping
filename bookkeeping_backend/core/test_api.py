# bookkeeping/tests/test_api.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import MoneyAccount

class MoneyAccountAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.money_account_data = {'name': 'Test Account', 'balance': 1000}
        self.money_account = MoneyAccount.objects.create(**self.money_account_data)
        self.valid_payload = {'name': 'Updated Test Account', 'balance': 2000}
        self.invalid_payload = {'name': '', 'balance': 2000}

    def test_get_money_accounts(self):
        response = self.client.get(reverse('moneyaccount-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_money_account(self):
        response = self.client.post(reverse('moneyaccount-list'), self.money_account_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_money_account(self):
        response = self.client.put(reverse('moneyaccount-detail', kwargs={'pk': self.money_account.pk}),
                                   self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_money_account(self):
        response = self.client.delete(reverse('moneyaccount-detail', kwargs={'pk': self.money_account.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)