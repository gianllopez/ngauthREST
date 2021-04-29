from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.decorators import action
from .serializers import LogupSerializer, LoginSerializer, VerifyHashSerializer, UserModel
from django.forms.models import model_to_dict

class UserViewset(GenericViewSet):

  serializer_class = LogupSerializer
  queryset = UserModel.objects.all()
      
  serializers = {
    'logup': LogupSerializer,
    'login': LoginSerializer,
    'verify-hash': VerifyHashSerializer
  }

  def get_serializer_class(self):
      path = self.request.get_full_path()[7:-1]
      return self.serializers[path]

  def user_response(self, user, status):
    data = model_to_dict(user, ['username', 'email', 'hash'])
    return Response(
      data={ 'user': data, 'status': status },
      status=HTTP_201_CREATED if status == 'CREATED' else HTTP_200_OK)

  @action(detail=False, methods=['post'])
  def logup(self, request):
    serializer = self.get_serializer_class()(data=request.data)
    serializer.is_valid(raise_exception=True)
    return self.user_response(serializer.save(), 'CREATED')
  
  @action(detail=False, methods=['post'])
  def login(self, request):
    serializer = self.get_serializer_class()(data=request.data)
    serializer.is_valid(raise_exception=True)
    return self.user_response(serializer.save(), 'AUTHENTICATED')

  @action(detail=False, methods=['post'], url_path='verify-hash')
  def verify_hash(self, request):
    user = UserModel.objects.filter(hash=request.data['hash'])
    valid = user.exists()
    data = {'valid': valid}
    if valid:
      data['name'] = user.first().name
    return Response(data=data, status=HTTP_200_OK if valid else HTTP_400_BAD_REQUEST)

