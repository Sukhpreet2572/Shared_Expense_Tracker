from django.db import models
from groups_app.models import Group, Membership


class Transaction(models.Model):

    TRANSACTION_TYPES = [
        ('EXPENSE', 'Expense'),
        ('SETTLEMENT', 'Settlement'),
        ('REFUND', 'Refund'),
        ('DEPOSIT', 'Deposit'),
    ]

    SPLIT_TYPES = [
        ('EQUAL', 'Equal'),
        ('UNEQUAL', 'Unequal'),
        ('PERCENTAGE', 'Percentage'),
        ('SHARE', 'Share'),
    ]

    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE
    )

    paid_by = models.ForeignKey(
        Membership,
        on_delete=models.CASCADE
    )

    transaction_type = models.CharField(
        max_length=20,
        choices=TRANSACTION_TYPES
    )

    description = models.CharField(
        max_length=255
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    currency = models.CharField(
        max_length=10
    )

    split_type = models.CharField(
        max_length=20,
        choices=SPLIT_TYPES
    )

    transaction_date = models.DateField()

    notes = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.description
class TransactionParticipant(models.Model):

    transaction = models.ForeignKey(
        Transaction,
        on_delete=models.CASCADE
    )

    participant = models.ForeignKey(
        Membership,
        on_delete=models.CASCADE
    )

    share_value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    percentage_value = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )

    owed_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.participant.name}"