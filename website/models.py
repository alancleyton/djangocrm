from django.db import models
from django.utils import timezone

class Company(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self) -> str:
        return str(self.name)

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
