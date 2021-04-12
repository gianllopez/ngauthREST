from django.db import models
import os, binascii

# Create your models here.

class UserModel(models.Model):
  
  name = models.CharField(max_length=30)
  username = models.CharField(max_length=12, unique=True,
    error_messages={'unique': 'This username is already taken'})
  email = models.EmailField(max_length=75)
  password = models.CharField(max_length=30)

  hash = models.CharField(max_length=6, unique=True)

  def save(self, *args, **kwargs):
    self.hash = binascii.hexlify(os.urandom(8))
    return super().save(*args, **kwargs)

  def __str__(self):
    return self.username
