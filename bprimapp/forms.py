from django.core import validators
from django import forms
from bprimapp.models import Student,Guest,HospitalityKit

class StudentRegistration(forms.ModelForm):
    class Meta:
        model=Student
        fields=['fname','mname','lname','email','mobile_number','gender','Bdate','Address','City','PinCode','State','Qualification','Course','Purpose','Duration']
        widgets={
            'fname':forms.TextInput(attrs={'class':'form-control'}),
            'mname':forms.TextInput(attrs={'class':'form-control'}),
            'lname':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'mobile_number':forms.NumberInput(attrs={'class':'form-control'}),
            'gender':forms.TextInput(attrs={'class':'form-control'}),
            'Bdate':forms.DateInput(attrs={'class':'form-control'}),
            'Address':forms.TextInput(attrs={'class':'form-control'}),
            'City':forms.TextInput(attrs={'class':'form-control'}),
            'PinCode':forms.NumberInput(attrs={'class':'form-control'}),
            'State':forms.TextInput(attrs={'class':'form-control'}),
            'Qualification':forms.TextInput(attrs={'class':'form-control'}),
            'Course':forms.TextInput(attrs={'class':'form-control'}),
            'Purpose':forms.TextInput(attrs={'class':'form-control'}),
            'Duration':forms.NumberInput(attrs={'class':'form-control'}),
        }

class GuestRegistration(forms.ModelForm):
    class Meta:
        model=Guest
        fields=['f_name','l_name','e_mail','mobile_no','Gender','institute_name','perm_address','city','pinCode','state','workshop','purpose','duration']
        widgets={
            'f_name':forms.TextInput(attrs={'class':'form-control'}),
            'l_name':forms.TextInput(attrs={'class':'form-control'}),
            'e_mail':forms.EmailInput(attrs={'class':'form-control'}),
            'mobile_no':forms.NumberInput(attrs={'class':'form-control'}),
            'Gender':forms.TextInput(attrs={'class':'form-control'}),
            'institute_name':forms.TextInput(attrs={'class':'form-control'}),
            'perm_address':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pinCode':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.TextInput(attrs={'class':'form-control'}),
            'workshop':forms.TextInput(attrs={'class':'form-control'}),
            'purpose':forms.TextInput(attrs={'class':'form-control'}),
            'duration':forms.NumberInput(attrs={'class':'form-control'}),
        }

class KitRegistration(forms.ModelForm):
    class Meta:
        model=HospitalityKit
        fields=['room_no','blankets','pillows','kettle','toothpaste','table','chairs','soap']
        widgets={
            'room_no':forms.TextInput(attrs={'class':'form-control'}),
            'blankets':forms.TextInput(attrs={'class':'form-control'}),
            'pillows':forms.TextInput(attrs={'class':'form-control'}),
            'kettle':forms.EmailInput(attrs={'class':'form-control'}),
            'toothpaste':forms.NumberInput(attrs={'class':'form-control'}),
            'table':forms.TextInput(attrs={'class':'form-control'}),
            'chairs':forms.DateInput(attrs={'class':'form-control'}),
            'soap':forms.TextInput(attrs={'class':'form-control'}),
        }