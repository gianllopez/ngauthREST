from rest_framework.serializers import ModelSerializer
from user.models import UserModel

class UserLogupSerializer(ModelSerializer):
  class Meta:
    model = UserModel
    fields = '__all__'
