# Generated by Django 4.1.1 on 2023-07-13 11:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_user_managers_alter_user_first_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.BooleanField(default=False, verbose_name='Понравился')),
                ('who', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='who', to=settings.AUTH_USER_MODEL, verbose_name='Кто оценил')),
                ('whom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='whom', to=settings.AUTH_USER_MODEL, verbose_name='Кого оценили')),
            ],
            options={
                'verbose_name': 'Оценка',
                'verbose_name_plural': 'Оценки',
                'db_table': 'grades',
            },
        ),
    ]