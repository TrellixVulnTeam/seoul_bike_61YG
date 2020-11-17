# Generated by Django 3.1.2 on 2020-11-16 23:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('username', models.CharField(max_length=64, verbose_name='사용자명')),
                ('password', models.CharField(max_length=64, verbose_name='비밀번호')),
                ('areaId', models.IntegerField(default=44, primary_key=True, serialize=False, verbose_name='담당지역')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='가입일자')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
