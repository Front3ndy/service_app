from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    company_name = models.CharField(max_length=255)
    full_address = models.CharField(max_length=255)

    def __str__(self):
        return f'Company - {self.company_name}'

