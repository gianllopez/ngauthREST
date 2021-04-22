from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.db.models import Q
from user.models import UserModel

class LogupSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserModel
    exclude = ['hash']
  
class LoginSerializer(serializers.Serializer):
  
  username_or_email = serializers.CharField(required=True)
  password = serializers.CharField(required=True)

  def validate(self, data):
    uoe = data['username_or_email']
    self.user = UserModel.objects.filter(
      Q(email=uoe) | Q(username=uoe), password=data['password'])
    if not self.user.exists():
      raise ValidationError({ 'user': 'Invalid username/email or password.'})
    return data
  
  def create(self, validated_data):
    return self.user.first()