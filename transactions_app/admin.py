from django.contrib import admin
from .models import Transaction, TransactionParticipant

admin.site.register(Transaction)
admin.site.register(TransactionParticipant)