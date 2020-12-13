# Generated by Django 3.1 on 2020-12-12 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stations',
            fields=[
                ('dataId', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('stationCode', models.CharField(max_length=10)),
                ('stationName', models.CharField(max_length=100)),
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
                ('areaId', models.ForeignKey(db_column='areaId', on_delete=django.db.models.deletion.PROTECT, to='user.users')),
            ],
            options={
                'db_table': 'station',
            },
        ),
        migrations.CreateModel(
            name='SubwayTot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField(default=0)),
                ('day', models.IntegerField(default=0)),
                ('tot_getoff', models.FloatField()),
                ('tot_ride', models.FloatField()),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='station.stations')),
            ],
            options={
                'db_table': 'subway_tot',
            },
        ),
        migrations.CreateModel(
            name='SubwayRideGetoff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField(default=0)),
                ('hour', models.IntegerField(default=0)),
                ('SubGetoff', models.IntegerField()),
                ('SubRide', models.IntegerField()),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='station.stations')),
            ],
            options={
                'db_table': 'subway_RideGetoff',
            },
        ),
    ]
