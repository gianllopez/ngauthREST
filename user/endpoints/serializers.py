from rest_framework import serializers
from user.models import UserModel

class LogupSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserModel
    exclude = ['hash']

