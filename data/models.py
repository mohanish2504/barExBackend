import email
import re
from django.db import models
from django.contrib import admin
from uuid import uuid4
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class EnquiryForm(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.TextField()
    email = models.EmailField()
    phone_number = PhoneNumberField()
    
    def __str__(self) -> str:
         return f"{self.name} -- {self.email} -- {self.phone_number}"

class EnquiryFormAdmin(admin.ModelAdmin):
    search_fields = ['name','email','phone_number']

    