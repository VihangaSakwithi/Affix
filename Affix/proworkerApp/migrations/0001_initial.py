# Generated by Django 4.1.7 on 2023-03-17 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProWorkers',
            fields=[
                ('ProWorkerId', models.AutoField(primary_key=True, serialize=False)),
                ('ProWorkerName', models.CharField(max_length=200)),
                ('UrbanCity', models.CharField(max_length=100)),
                ('JoinDate', models.DateField()),
                ('ImageName', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='UrbanCity',
            fields=[
                ('UrbanCityId', models.AutoField(primary_key=True, serialize=False)),
                ('UrbanCityName', models.CharField(max_length=100)),
            ],
        ),
    ]
