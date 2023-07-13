from django.core.mail import EmailMessage
from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, status, parsers, filters
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from APPTRIX import settings
from api.filters import UserFilter
from api.models import User, Grade
from api.packs import Error, Successful, EmailSendThread
from api.serializers.grade_serializer import GradeSerializer
from api.serializers.user_serializers import UserResponseSerializer, UserCreateSerializer


class CustomCreateModelMixin(mixins.CreateModelMixin):
    parser_classes = [parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)



@method_decorator(name='retrieve',
                  decorator=swagger_auto_schema(
                      tags=['clients'],
                      operation_id='Получить пользователя по id'
                  ))
class UserCreateView(mixins.RetrieveModelMixin,
                     CustomCreateModelMixin,
                     GenericViewSet):
    serializer_class = UserResponseSerializer
    queryset = User.objects.filter(is_staff=False)

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
            return Error(data={'message': serializer.errors})

        data = serializer.validated_data

        user = User()

        for attr in data:
            setattr(user, attr, data.get(attr))

        user.set_password(user.password)

        user.save()

        return Successful(UserResponseSerializer(user).data)


class UserMatchView(GenericViewSet):
    serializer_class = GradeSerializer
    permission_classes = [IsAuthenticated]
    queryset = Grade.objects.all()

    @action(detail=True, methods=['POST'], url_path='match')
    @swagger_auto_schema(
        tags=['clients'],
        request_body=GradeSerializer,
        responses={
            status.HTTP_200_OK: GradeSerializer
        },
        operation_id='Оценить человека'
    )
    def match(self, request, pk):
        me = request.user
        whom = User.objects.filter(id=pk)

        if not whom.exists():
            return Error(data={'message': 'Этот пользователь не существует'})

        whom = whom.first()

        if whom.id == me.id:
            return Error(data={'message': 'Вы не можете оценить сами себя'})

        if Grade.objects.filter(who=me, whom=whom).exists():
            return Error(data={'message': 'Вы не можете оценить одного человека дважды'})

        serializer = GradeSerializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except:
            return Error(data={'message': serializer.errors})

        data = serializer.validated_data

        grade = Grade()
        grade.who = me
        grade.whom = whom
        grade.grade = data['grade']
        grade.save()

        # Если пользователь отметил понравился,
        # то проверить взаимно ли это
        if data['grade']:
            grade_whom = Grade.objects.filter(who=whom, whom=me, grade=True)

            if grade_whom.exists():
                message_first = f'Вы понравились {whom.first_name}! Почта участника: {whom.email}'
                message_second = f'Вы понравились {me.first_name}! Почта участника: {me.email}'

                email_message_first = EmailMessage(
                    'Взаимная симпатия',
                    message_first,
                    settings.EMAIL_HOST_USER,
                    [me.email],
                )

                email_message_second = EmailMessage(
                    'Взаимная симпатия',
                    message_second,
                    settings.EMAIL_HOST_USER,
                    [whom.email],
                )

                EmailSendThread(email_message_first).start()
                EmailSendThread(email_message_second).start()

        return Successful()


@method_decorator(name='list',
                  decorator=swagger_auto_schema(
                      tags=['list'],
                      operation_id='Получить список пользователей'
                  ))
class UserListView(mixins.ListModelMixin, GenericViewSet):
    serializer_class = UserResponseSerializer
    queryset = User.objects.filter(is_staff=False)
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter
