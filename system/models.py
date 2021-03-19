from django.db import models

from encrypted_fields import fields
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse
from django.db.models.signals import post_save
# Create your models here.



GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

class User(AbstractUser):
    speciality = models.ForeignKey("Department", on_delete=models.SET_NULL, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone = fields.EncryptedCharField(max_length=20, blank=True, null=True)

    REQUIRED_FIELDS=['email']

    def __str__(self):
        return f"{self.first_name}"


class Status(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'status'
        verbose_name_plural = 'statuses'



class Department(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name





class Appointment(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    email = fields.EncryptedEmailField()
    age = models.IntegerField()
    phone = fields.EncryptedCharField(max_length=20)
    department = models.ForeignKey("Department", on_delete=models.SET_NULL, blank=True, null=True)
    gender = fields.EncryptedCharField(max_length=20, choices=GENDER_CHOICES)
    date = models.DateTimeField()
    status = models.ForeignKey('Status', on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    nurse = models.ForeignKey('Nurse', on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.name


class Nurse(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



# def post_user_created_signal(sender, instance, created, **kwargs):
#     if created:
#         Doctor.objects.create(
#             user=instance,
#             speciality=instance.speciality,
#             email=instance.email,
#             phone=instance.phone,
#         )
# post_save.connect(post_user_created_signal, sender=User)