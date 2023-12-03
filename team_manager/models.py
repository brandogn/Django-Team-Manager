from django.db import models

# Create your models here.
class TeamMember(models.Model):
    ROLES = [
        ('regular', 'Regular'),
        ('admin', 'Admin'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    role = models.CharField(max_length=10, choices=ROLES, default='regular')

