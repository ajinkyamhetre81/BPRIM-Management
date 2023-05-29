# Generated by Django 4.1.2 on 2022-12-29 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bprimapp', '0004_rename_roomno_student_room_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_id', models.IntegerField(blank=True, unique=True)),
                ('fname', models.CharField(max_length=70)),
                ('mname', models.CharField(max_length=70)),
                ('lname', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=122, unique=True)),
                ('mobile_number', models.IntegerField(unique=True)),
                ('gender', models.CharField(max_length=10)),
                ('Bdate', models.DateField()),
                ('Address', models.CharField(max_length=70)),
                ('City', models.CharField(max_length=70)),
                ('PinCode', models.IntegerField()),
                ('State', models.CharField(max_length=70)),
                ('Qualification', models.CharField(max_length=70)),
                ('Course', models.CharField(max_length=70)),
                ('Purpose', models.CharField(max_length=70)),
                ('Duration', models.IntegerField()),
                ('room_no', models.CharField(blank=True, max_length=2)),
            ],
        ),
    ]