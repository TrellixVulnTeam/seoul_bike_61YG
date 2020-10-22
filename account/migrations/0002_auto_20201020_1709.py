# Generated by Django 3.1.2 on 2020-10-20 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bikeuser',
            name='areaid',
            field=models.CharField(max_length=10, verbose_name='담당지역'),
        ),
        migrations.AlterField(
            model_name='bikeuser',
            name='password',
            field=models.CharField(max_length=64, verbose_name='비밀번호'),
        ),
        migrations.AlterField(
            model_name='bikeuser',
            name='register_dttm',
            field=models.DateField(auto_now_add=True, verbose_name='가입일자'),
        ),
        migrations.AlterField(
            model_name='bikeuser',
            name='username',
            field=models.CharField(max_length=64, verbose_name='사용자명'),
        ),
    ]
