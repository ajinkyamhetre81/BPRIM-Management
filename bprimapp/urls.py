from django.contrib import admin
from django.urls import path, include
from bprimapp import views

urlpatterns = [
    path('',views.index, name="home"),
    path('login',views.loginUser, name="login"),
    path('logout',views.logoutUser, name="logout"),
    path("about",views.about, name='about'),
    path("services",views.services, name='services'),
    path("contact",views.contact, name='contact'),
    path("hostel",views.hostel, name='hostel'),
    path("guest_house",views.guest_house, name='guest_house'),
    path("register_student",views.register_student, name='register_student'),
    path("display_student",views.display_student, name='display_student'),
    path("register_guest",views.register_guest, name='register_guest'),
    path("display_guest",views.display_guest, name='display_guest'),
    path("alumni",views.alumni,name='alumni'),
    path("past_guest",views.past_guest,name='past_guest'),
    path("move/<int:id>/",views.move,name='move'),
    path("move_guest/<int:id>/",views.move_guest,name='move_guest'),
    path("open_student/<str:rno>",views.open_student, name='open_student'),
    path("open_guest/<str:Rno>",views.open_guest, name='open_guest'),
    path("register_kits",views.register_kits, name='register_kits'),
    path("add",views.add,name='add'),
    path("addRoomModel",views.addRoom,name='addRoomModel'),
    path("edit",views.edit, name='edit'),
    path("update/<str:id>",views.update, name='update'),
    path("delete/<str:id>",views.delete,name='delete'),
    path("edit_st",views.edit_st, name='edit_st'),
    path("update_st/<str:id>",views.update_st, name='update_st'),
    path("edit_guest",views.edit_guest, name='edit_guest'),
    path("update_guest/<str:id>",views.update_guest, name='update_guest'),
    path("stu_print/<int:id>",views.stu_print, name='stu_print'),
    path("pdf_stud/<int:id>",views.pdf_stud,name='pdf_stud'),
    path("guest_print/<int:id>",views.guest_print, name='guest_print'),
    path("pdf_guest/<int:id>",views.pdf_guest,name='pdf_guest')
]