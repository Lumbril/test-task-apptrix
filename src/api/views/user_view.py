from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from api.models import User
from api.serializers.user_serializers import UserResponse


@method_decorator(name='list',
                  decorator=swagger_auto_schema(
                      operation_id='Получить список пользователей'
                  ))
@method_decorator(name='retrieve',
                  decorator=swagger_auto_schema(
                      operation_id='Получить пользователя по id'
                  ))
class UserView(mixins.RetrieveModelMixin,
               mixins.ListModelMixin,
               GenericViewSet):
    serializer_class = UserResponse
    queryset = User.objects.all()
