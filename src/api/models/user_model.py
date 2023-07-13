from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

from api.packs import watermark_photo


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, blank=False, null=False, verbose_name='Почта')
    first_name = models.CharField(max_length=30, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=30, blank=True, verbose_name='Фамилия')
    avatar = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Аватар')
    gender = models.BooleanField(default=True, verbose_name='Пол (0 - ж, 1 - м)')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def get_avatar(self):
        return str(self.avatar) if self.avatar else None

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.avatar:
            avatar = watermark_photo(self.avatar.path)
            avatar.save(self.avatar.path)

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
