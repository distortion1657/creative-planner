from django.contrib import admin
from .models import CustomUser, ProductiveObject
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(ProductiveObject)