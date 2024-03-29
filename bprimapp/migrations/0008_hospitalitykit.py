# Generated by Django 4.1.2 on 2022-12-31 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bprimapp', '0007_pastguest'),
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalityKit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.CharField(blank=True, max_length=2)),
                ('blankets', models.IntegerField()),
                ('pillows', models.IntegerField()),
                ('kettle', models.CharField(max_length=10)),
                ('toothpaste', models.CharField(max_length=10)),
                ('table', models.IntegerField()),
                ('chairs', models.IntegerField()),
                ('soap', models.IntegerField()),
            ],
        ),
    ]
