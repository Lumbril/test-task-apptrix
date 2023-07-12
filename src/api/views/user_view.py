from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, status, parsers
from rest_framework.viewsets import GenericViewSet

from api.models import User
from api.packs import Error, Successful
from api.serializers.user_serializers import UserResponseSerializer, UserCreateSerializer


class CustomCreateModelMixin(mixins.CreateModelMixin):
    parser_classes = [parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


@method_decorator(name='list',
                  decorator=swagger_auto_schema(
                      tags=['clients'],
                      operation_id='Получить список пользователей'
                  ))
@method_decorator(name='retrieve',
                  decorator=swagger_auto_schema(
                      tags=['clients'],
                      operation_id='Получить пользователя по id'
                  ))
class UserCreateView(mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     CustomCreateModelMixin,
                     GenericViewSet):
    serializer_class = UserResponseSerializer
    queryset = User.objects.all()

    @swagger_auto_schema(
        tags=['clients'],
        request_body=UserCreateSerializer,
        responses={
            status.HTTP_200_OK: UserResponseSerializer,
        },
        operation_id='Создать пользователя'
    )
    def create(self, request):
        serializer = UserCreateSerializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except:
            return Error(data={'message': serializer.errors, 'exit': False})

        data = serializer.validated_data

        user = User()

        for attr in data:
            setattr(user, attr, data.get(attr))

        user.save()

        return Successful(UserResponseSerializer(user).data)
