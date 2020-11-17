# Generated by Django 3.1.2 on 2020-11-16 23:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('stationLatitude', models.FloatField(max_length=20)),
                ('stationLongitude', models.FloatField(max_length=20)),
                ('rackTotCnt', models.IntegerField(default=0)),
                ('distance_hanriver', models.IntegerField(default=0)),
                ('distance_bikeroad', models.IntegerField(default=0)),
                ('distance_subway', models.IntegerField(default=0)),
                ('distance_school_mid', models.IntegerField(default=0)),
                ('distance_school_high', models.IntegerField(default=0)),
                ('distance_school_univ', models.IntegerField(default=0)),
                ('PopTot', models.IntegerField(default=0)),
                ('areaId', models.ForeignKey(db_column='areaId', on_delete=django.db.models.deletion.PROTECT, to='account.users')),
            ],
            options={
                'db_table': 'area',
            },
        ),
        migrations.CreateModel(
            name='StationNow',
            fields=[
                ('stationName', models.CharField(max_length=100)),
                ('parkingBikeTotCnt', models.IntegerField(default=0)),
                ('stationCode', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.localtime)),
            ],
            options={
                'db_table': 'station_now',
            },
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ta', models.FloatField()),
                ('rn', models.FloatField()),
                ('ws', models.FloatField()),
                ('wd', models.FloatField()),
                ('hm', models.FloatField()),
                ('ss', models.FloatField()),
                ('icsr', models.FloatField()),
                ('dsnw', models.FloatField()),
                ('hr3Fhsc', models.FloatField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.localtime, editable=False)),
            ],
            options={
                'db_table': 'weather',
            },
        ),
        migrations.CreateModel(
            name='DailyStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parkingBikeTotCnt', models.IntegerField(default=0)),
                ('created_at', models.CharField(max_length=20)),
                ('dataId', models.ForeignKey(db_column='dataId', on_delete=django.db.models.deletion.CASCADE, to='bikeapp.area')),
            ],
            options={
                'db_table': 'daily_station',
            },
        ),
        migrations.AddField(
            model_name='area',
            name='stationCode',
            field=models.ForeignKey(db_column='stationCode', on_delete=django.db.models.deletion.CASCADE, to='bikeapp.stationnow'),
        ),
    ]
