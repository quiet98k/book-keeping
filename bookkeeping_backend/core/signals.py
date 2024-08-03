from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Transaction

@receiver(pre_save, sender=Transaction)
def update_balance(sender, instance, **kwargs):
    if instance.pk:  # Existing transaction
        old_instance = Transaction.objects.get(pk=instance.pk)
        instance.account.update_balance(instance.amount - old_instance.amount)
    else:  # New transaction
        instance.account.update_balance(instance.amount)
