# Generated by Django 3.1 on 2020-12-12 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='core.timestampedmodel')),
                ('username', models.CharField(max_length=64, verbose_name='사용자명')),
                ('password', models.CharField(max_length=64, verbose_name='비밀번호')),
                ('name', models.CharField(default=None, max_length=64, null=True)),
                ('areaId', models.IntegerField(default=44, primary_key=True, serialize=False, verbose_name='담당지역')),
            ],
            options={
                'db_table': 'users',
            },
            bases=('core.timestampedmodel',),
        ),
    ]
