from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK
from rest_framework.decorators import action
from .serializers import LogupSerializer, LoginSerializer, UserModel
from django.forms.models import model_to_dict

class UserViewset(GenericViewSet):

  serializer_class = LogupSerializer
  queryset = UserModel.objects.all()

  def get_serializer_class(self):
    path = self.request.get_full_path()
    return LogupSerializer if 'logup' in path else LoginSerializer

  def user_response(self, user, status):
    data = model_to_dict(user, ['username', 'email', 'hash'])
    return Response(
      data={ 'user': data, 'status': status },
      status=HTTP_201_CREATED if status == 'CREATED' else HTTP_200_OK)

  @action(detail=False, methods=['post'])
  def logup(self, request):
    serializer = self.get_serializer_class()(data=request.data)
    serializer.is_valid(raise_exception=True)
    return user_response(serializer.save(), 'CREATED')
  
  @action(detail=False, methods=['post'])
  def login(self, request):
    serializer = self.get_serializer_class()(data=request.data)
    serializer.is_valid(raise_exception=True)
    return user_response(serializer.save(), 'VALIDATED')
