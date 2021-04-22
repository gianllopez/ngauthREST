from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.decorators import action
from .serializers import LogupSerializer, LoginSerializer, UserModel
from django.forms.models import model_to_dict

class UserViewset(GenericViewSet):

  serializer_class = LogupSerializer
  queryset = UserModel.objects.all()

  def get_serializer_class(self):
    path = self.request.get_full_path()
    return LogupSerializer if 'logup' in path else LoginSerializer

  @action(detail=False, methods=['post'])
  def logup(self, request):
    self.get_serializer_class()
    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response(data={
      'user': model_to_dict(user, ['username', 'email', 'hash']),
      'status': 'CREATED', }, status=HTTP_201_CREATED)
  
  @action(detail=False, methods=['post'])
  def login(self, request):
    import pdb; pdb.set_trace()