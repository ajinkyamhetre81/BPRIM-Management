from django.contrib import admin
from bprimapp.models import Student,Alumni,Guest,PastGuest,HospitalityKit

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=["id","reg_id","fname","mname","lname","email","mobile_number","father_occupation",
                  "locl_grd","locl_grd_add","Institute","gender","Bdate","Address","City","State",
                  "PinCode","Qualification","Course","Purpose","arrival_year","leaving_year",
                  "Duration","room_no","recommend"]
    search_fields=["reg_id","fname","mname","lname","email","mobile_number","father_occupation",
                  "locl_grd","locl_grd_add","Institute","gender","Bdate","Address","City","State",
                  "PinCode","Qualification","Course","Purpose","arrival_year","leaving_year",
                    "Duration","room_no","recommend"]
    list_editable=["reg_id","fname","mname","lname","email","mobile_number","father_occupation",
                  "locl_grd","locl_grd_add","Institute","gender","Bdate","Address","City","State",
                  "PinCode","Qualification","Course","Purpose","arrival_year","leaving_year",
                    "Duration","room_no","recommend"]

admin.site.register(Student,StudentAdmin)



class AlumniAdmin(admin.ModelAdmin):
    list_display=["id","reg_id","fname","mname","lname","email","mobile_number","father_occupation",
                  "locl_grd","locl_grd_add","Institute","gender","Bdate","Address","City","State",
                  "PinCode","Qualification","Course","Purpose","arrival_year","leaving_year",
                  "Duration","room_no","recommend"]
    search_fields=["reg_id","fname","mname","lname","email","mobile_number","father_occupation",
                  "locl_grd","locl_grd_add","Institute","gender","Bdate","Address","City","State",
                  "PinCode","Qualification","Course","Purpose","arrival_year","leaving_year",
                    "Duration","room_no","recommend"]
    # list_editable=["reg_id","fname","mname","lname","email","mobile_number","father_occupation",
    #               "locl_grd","locl_grd_add","Institute","gender","Bdate","Address","City","State",
    #               "PinCode","Qualification","Course","Purpose","arrival_year","leaving_year",
    #                 "Duration","room_no","recommend"]

admin.site.register(Alumni,AlumniAdmin)



class GuestAdmin(admin.ModelAdmin):
    
    list_display=["id","reg_number","f_name","l_name","e_mail","mobile_no",
                    "Gender","institute_name","perm_address","city","state","pinCode","workshop"
                    ,"purpose","arrival_date","leaving_date","duration","roomno"]
    search_fields=["reg_number","f_name","l_name","e_mail","mobile_no",
                    "Gender","institute_name","perm_address","city","state","pinCode","workshop"
                    ,"purpose","arrival_date","leaving_date","duration","roomno"]
    list_editable=["f_name","l_name","e_mail","mobile_no",
                    "Gender","institute_name","perm_address","city","state","pinCode","workshop"
                    ,"purpose","arrival_date","leaving_date","duration","roomno"]

admin.site.register(Guest,GuestAdmin)



class PastGuestAdmin(admin.ModelAdmin):
    
    list_display=["id","reg_number","f_name","l_name","e_mail","mobile_no",
                    "Gender","institute_name","perm_address","city","state","pinCode","workshop"
                    ,"purpose","arrival_date","leaving_date","duration","roomno"]
    search_fields=["reg_number","f_name","l_name","e_mail","mobile_no",
                    "Gender","institute_name","perm_address","city","state","pinCode","workshop"
                    ,"purpose","arrival_date","leaving_date","duration","roomno"]

admin.site.register(PastGuest,PastGuestAdmin)



class KitAdmin(admin.ModelAdmin):
    list_display=["id","room_no","blankets","pillows","kettle","toothpaste","table","chairs",
                    "soap"]
    search_fields=["room_no","blankets","pillows","kettle","toothpaste","table","chairs",
                    "soap"]
admin.site.register(HospitalityKit,KitAdmin)