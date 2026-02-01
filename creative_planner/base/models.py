from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=255)
    due_date = models.DateTimeField(null=True, blank=True)