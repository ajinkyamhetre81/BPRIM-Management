
from django.db import models
from datetime import date

# Create your models here.  
# What is model? - it simply defines database

class Student(models.Model):
    Q=(
        ("SSC","High_School"),("HSC","Higher_School"),("Bachelors","Graduation"),("PG","Post_Graduation"),("Dr","Phd")
    )
    g=(
        ("M","Male"),("F","Female")
    )
    reg_id=models.IntegerField(unique=True,blank=True,default=00000)
    fname=models.CharField(max_length=70,default='NA')
    mname=models.CharField(max_length=70,default='NA')
    lname=models.CharField(max_length=70,default='NA')
    email=models.EmailField(max_length=122,default='NA',unique=True)
    mobile_number=models.IntegerField(unique=True)
    father_occupation=models.CharField(max_length=70,default='NA')
    locl_grd=models.CharField(max_length=70,default='NA')
    locl_grd_add=models.CharField(max_length=70,default='NA')
    Institute=models.CharField(max_length=70,default='NA')
    gender=models.CharField(max_length=10,default='NA',choices=g)
    Bdate=models.DateField(default='2022-01-01')
    Address=models.CharField(max_length=70,default='NA')
    City=models.CharField(max_length=70,default='NA')
    PinCode=models.IntegerField()
    State=models.CharField(max_length=70,default='NA')
    Qualification=models.CharField(max_length=70,default='NA',choices=Q)
    Course=models.CharField(max_length=70,default='NA')
    Purpose=models.CharField(max_length=70,default='NA')
    arrival_year=models.IntegerField(blank=True,default=2000)
    leaving_year=models.IntegerField(blank=True,default=2000)
    Duration=models.IntegerField()
    room_no=models.CharField(max_length=2,blank=True,default='NA')
    recommend=models.CharField(max_length=70,default='NA')

    def _str_(self):
        return self.name 

class Alumni(models.Model):
    reg_id=models.IntegerField(unique=True,blank=True)
    fname=models.CharField(max_length=70)
    mname=models.CharField(max_length=70)
    lname=models.CharField(max_length=70)
    email=models.EmailField(max_length=122,unique=True)
    mobile_number=models.IntegerField(unique=True)
    father_occupation=models.CharField(max_length=70,default='NA')
    locl_grd=models.CharField(max_length=70,default='NA')
    locl_grd_add=models.CharField(max_length=70,default='NA')
    Institute=models.CharField(max_length=70,default='NA')
    gender=models.CharField(max_length=10)
    Bdate=models.DateField()
    Address=models.CharField(max_length=70)
    City=models.CharField(max_length=70)
    PinCode=models.IntegerField()
    State=models.CharField(max_length=70)
    Qualification=models.CharField(max_length=70)
    Course=models.CharField(max_length=70)
    Purpose=models.CharField(max_length=70)
    arrival_year=models.IntegerField(blank=True,default=2000)
    leaving_year=models.IntegerField(blank=True,default=2000)
    Duration=models.IntegerField()
    room_no=models.CharField(max_length=2,blank=True)
    recommend=models.CharField(max_length=70,default='NA')

class Guest(models.Model):
    gen=(
        ("M","Male"),("F","Female")
    )
    reg_number=models.IntegerField(null=True)
    f_name=models.CharField(max_length=70,default='NA')
    l_name=models.CharField(max_length=70,default='NA')
    e_mail=models.EmailField(max_length=122,default='NA',unique=True)
    mobile_no=models.IntegerField(unique=True)
    # resi_no=models.IntegerField(blank=True)
    Gender=models.CharField(max_length=10,default='NA',choices=gen)
    institute_name=models.CharField(max_length=70,default='NA')
    perm_address=models.CharField(max_length=70,default='NA')
    city=models.CharField(max_length=70,default='NA')
    state=models.CharField(max_length=70,default='NA')
    pinCode=models.IntegerField()
    workshop=models.CharField(max_length=70,default='NA')
    purpose=models.CharField(max_length=70,default='NA')
    arrival_date=models.DateField(default='2022-01-01')
    leaving_date=models.DateField(default='2022-01-01')
    duration=models.CharField(max_length=20,blank=True)
    roomno=models.CharField(max_length=2,blank=True,default='NA')

    def _str_(self):
        return self.name

class PastGuest(models.Model):
    reg_number=models.IntegerField(null=True)
    f_name=models.CharField(max_length=70)
    l_name=models.CharField(max_length=70)
    e_mail=models.EmailField(max_length=122,unique=True)
    mobile_no=models.IntegerField(unique=True)
    # resi_no=models.IntegerField(unique=True)
    Gender=models.CharField(max_length=10)
    institute_name=models.CharField(max_length=70)
    perm_address=models.CharField(max_length=70)
    city=models.CharField(max_length=70)
    pinCode=models.IntegerField()
    state=models.CharField(max_length=70)
    workshop=models.CharField(max_length=70)
    purpose=models.CharField(max_length=70)
    arrival_date=models.DateField(default='2022-01-01')
    leaving_date=models.DateField(default='2022-01-01')
    duration=models.IntegerField(blank=True)
    roomno=models.CharField(max_length=2,blank=True)

class HospitalityKit(models.Model):
    room_no=models.CharField(max_length=2,blank=True)
    blankets=models.IntegerField()
    pillows=models.IntegerField()
    kettle=models.CharField(max_length=10)
    toothpaste=models.CharField(max_length=10)
    table=models.IntegerField()
    chairs=models.IntegerField()
    soap=models.IntegerField()

class Create_Room(models.Model):
    room_no=models.CharField(max_length=2,blank=True)
