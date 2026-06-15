from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Membership(models.Model):

    MEMBER_TYPES = [
        ('PERMANENT', 'Permanent'),
        ('TEMPORARY', 'Temporary'),
        ('GUEST', 'Guest'),
    ]

    name = models.CharField(max_length=100)

    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='memberships'
    )

    joined_at = models.DateField()

    left_at = models.DateField(
        null=True,
        blank=True
    )

    member_type = models.CharField(
        max_length=20,
        choices=MEMBER_TYPES,
        default='PERMANENT'
    )

    def __str__(self):
        return self.name