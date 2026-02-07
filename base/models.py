from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid
from datetime import timedelta
# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=25, unique=True, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    creation = models.DateTimeField(auto_now_add=True)
    premium = models.BooleanField(default=False)
    #I'm unsure if this should be durationField or timeField
    freetime = models.DurationField(default=timedelta())
    productivity = models.FloatField(default=0.0)
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f"${self.username}"

class ProductiveObject(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE) # Cascade means if the parent gets deleted, automatically delete everything that depends on it
    name = models.CharField(max_length=255)
    public_id = models.UUIDField(
        default=uuid.uuid4(), # uuid4 generates a uuid completely randomly, hence is used here
        primary_key=True,
        editable=False,
        unique=True)
    productivity_value = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)]
    )
    duration = models.DurationField(default=timedelta())
    creation = models.DateTimeField(auto_now_add=True)

class Task(models.Model):
    name = models.CharField(max_length=255)
    due_date = models.DateTimeField(null=True, blank=True)
