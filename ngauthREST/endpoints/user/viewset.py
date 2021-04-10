from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.decorators import action
from .serializers import UserLogupSerializer, UserModel

class UserViewset(GenericViewSet):

  queryset = UserModel.objects.all()

  @action(detail=False, methods=['post'])
  def logup(self, request):
    serializer = UserLogupSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response(data={
      'user': {
        'username': user.username,
        'email': user.email
      },
      'status': 'CREATED'
    }, status=HTTP_201_CREATED)
