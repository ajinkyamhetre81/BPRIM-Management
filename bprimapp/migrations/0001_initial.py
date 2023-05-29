# Generated by Django 4.1.2 on 2022-12-28 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(default='NA', max_length=70)),
                ('mname', models.CharField(default='NA', max_length=70)),
                ('lname', models.CharField(default='NA', max_length=70)),
                ('email', models.EmailField(default='NA', max_length=122)),
                ('mobile_number', models.IntegerField(unique=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='NA', max_length=10)),
                ('Bdate', models.DateField(default='2022-01-01')),
                ('Address', models.CharField(default='NA', max_length=70)),
                ('City', models.CharField(default='NA', max_length=70)),
                ('PinCode', models.IntegerField()),
                ('State', models.CharField(default='NA', max_length=70)),
                ('Qualification', models.CharField(choices=[('SSC', 'High_School'), ('HSC', 'Higher_School'), ('Bachelors', 'Graduation'), ('PG', 'Post_Graduation'), ('Dr', 'Phd')], default='NA', max_length=70)),
                ('Course', models.CharField(default='NA', max_length=70)),
                ('Purpose', models.CharField(default='NA', max_length=70)),
                ('Duration', models.IntegerField()),
            ],
        ),
    ]
