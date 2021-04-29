from django.db import models
import os, binascii

# Create your models here.

class UserModel(models.Model):
  
  name = models.CharField(max_length=75)
  username = models.CharField(max_length=12, unique=True,
    error_messages={'unique': 'This username is already taken.'})
  email = models.EmailField(max_length=75)
  password = models.CharField(max_length=30)

  hash = models.CharField(max_length=16, unique=True)

  def save(self, *args, **kwargs):
    self.hash = binascii.hexlify(os.urandom(8)).decode()
    self.name = self.name.capitalize()
    self.username = self.username.lower()
    return super().save(*args, **kwargs)

  def __str__(self):
    return self.username
