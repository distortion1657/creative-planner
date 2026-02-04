from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)
    creation = models.DateTimeField(auto_now_add=True)
    premium = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f"${self.username}"

class ProductiveObject(models.Model):
    name = models.CharField(max_length=255)
    productivity_value = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)]
    )
    creation = models.DateTimeField(auto_now_add=True)

class Task(models.Model):
    name = models.CharField(max_length=255)
    due_date = models.DateTimeField(null=True, blank=True)
