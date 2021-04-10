from django.db import models

# Create your models here.

class UserModel(models.Model):
  
  name = models.CharField(max_length=30)
  username = models.CharField(max_length=12, unique=True)
  email = models.EmailField(max_length=75)
  password = models.CharField(max_length=30)

  def __str__(self):
    return self.username
