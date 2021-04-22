from rest_framework import serializers
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
    query = Q(email=data['email']) | Q(username=data['username'])
    user = UserModel.objects.filter(query, password=data['password'])
    import pdb; pdb.set_trace()


