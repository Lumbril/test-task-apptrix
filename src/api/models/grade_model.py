from django.db import models

from api.models import User


class Grade(models.Model):
    who = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='who',
                            blank=False, null=True, verbose_name='Кто оценил')
    whom = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='whom',
                             blank=False, null=True, verbose_name='Кого оценили')
    grade = models.BooleanField(default=False, verbose_name='Понравился')

    class Meta:
        db_table = 'grades'
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
