from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.decorators import action
from .serializers import LogupSerializer, UserModel
from django.forms.models import model_to_dict

class UserViewset(GenericViewSet):

  serializer_class = LogupSerializer
  queryset = UserModel.objects.all()

  @action(detail=False, methods=['post'])
  def logup(self, request):
    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response(data={
      'user': model_to_dict(user, ['username', 'email', 'hash']),
      'status': 'CREATED', }, status=HTTP_201_CREATED)
