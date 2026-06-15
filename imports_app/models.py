from django.db import models


class ImportBatch(models.Model):

    file_name = models.CharField(max_length=255)

    total_rows = models.IntegerField(default=0)

    successful_rows = models.IntegerField(default=0)

    failed_rows = models.IntegerField(default=0)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name
class Anomaly(models.Model):

    SEVERITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ]

    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('RESOLVED', 'Resolved'),
        ('IGNORED', 'Ignored'),
    ]

    import_batch = models.ForeignKey(
        ImportBatch,
        on_delete=models.CASCADE
    )

    anomaly_type = models.CharField(
        max_length=100
    )

    severity = models.CharField(
        max_length=20,
        choices=SEVERITY_CHOICES
    )

    description = models.TextField()

    suggested_action = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='OPEN'
    )

    def __str__(self):
        return self.anomaly_type