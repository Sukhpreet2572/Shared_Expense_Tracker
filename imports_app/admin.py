from django.contrib import admin
from .models import ImportBatch, Anomaly

admin.site.register(ImportBatch)
admin.site.register(Anomaly)