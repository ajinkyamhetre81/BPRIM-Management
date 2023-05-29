from django.shortcuts import render,redirect,HttpResponseRedirect,get_object_or_404
from django.contrib.auth import logout,authenticate,login
from bprimapp.models import Student,Alumni,Guest,PastGuest,HospitalityKit,Create_Room
from datetime import date
from django.db.models import Max
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.

def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')


def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        #check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect("/login")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is about page")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("This is services page")

def hostel(request):
    stdata1=Student.objects.filter(room_no='H1').count
    stdata2=Student.objects.filter(room_no='H2').count
    stdata3=Student.objects.filter(room_no='H3').count
    stdata4=Student.objects.filter(room_no='H4').count
    stdata5=Student.objects.filter(room_no='H5').count
 
    return render(request, 'hostel.html',{'stctr1':stdata1,'stctr2':stdata2,'stctr3':stdata3,'stctr4':stdata4,'stctr5':stdata5}) 
    #return HttpResponse("This is hostel page")

def guest_house(request):
    gstdata1=Guest.objects.filter(roomno='G1').count
    gstdata2=Guest.objects.filter(roomno='G2').count
    gstdata3=Guest.objects.filter(roomno='G3').count
    gstdata4=Guest.objects.filter(roomno='G4').count
    gstdata5=Guest.objects.filter(roomno='G5').count
    return render(request, 'guest_house.html',{'gstctr1':gstdata1,'gstctr2':gstdata2,'gstctr3':gstdata3,'gstctr4':gstdata4,'gstctr5':gstdata5})
   # return HttpResponse("This is guest house page")

def contact(request):
    return render(request, 'contact.html') 
   # return HttpResponse("This is contact page")

def register_student(request):
    reg_no=2001 if Student.objects.count() == 0 else Student.objects.aggregate(max=Max('reg_id'))["max"]+1
    if request.method =='POST':
        stctr=Student.objects.filter(room_no=request.POST.get('room_no')).count()

        if request.POST.get('room_no') == 'H4':
            if(stctr > 2):
                return render(request,'display_student.html',{'error':"True",'r_no':request.POST.get('room_no')})
        else:
            if(stctr > 3):
                return render(request,'display_student.html',{'error':"True",'r_no':request.POST.get('room_no')})
        fname=request.POST.get('FirstName')
        mname=request.POST.get('MiddleName')
        lname=request.POST.get('LastName')
        email=request.POST.get('EmailID')
        mobile_number=request.POST.get('MobileNumber')
        father_occupation=request.POST.get('father_occupation')
        locl_grd=request.POST.get('local_guardian')
        locl_grd_add=request.POST.get('local_guardian_addr')
        Institute=request.POST.get('Institute_name')
        gender=request.POST.get('Gender')
        Bdate = request.POST.get('birthdate')
        Address=request.POST.get('Address')
        City=request.POST.get('City')
        PinCode=request.POST.get('PinCode')
        State=request.POST.get('State')
        Qualification=request.POST.get('Qualification')
        Course=request.POST.get('Course')
        Purpose=request.POST.get('Purpose')
        arrival_year=request.POST.get('arrival_year')
        leaving_year=request.POST.get('leaving_year')
        Duration=int(leaving_year)-int(arrival_year)
        room_no=request.POST.get('room_no')
        recommend=request.POST.get('Recommendation')

        reg=Student(reg_id=reg_no,fname=fname,mname=mname,lname=lname,email=email,mobile_number=mobile_number,father_occupation=father_occupation,locl_grd=locl_grd,locl_grd_add=locl_grd_add,Institute=Institute,gender=gender,Bdate=Bdate,Address=Address,City=City,PinCode=PinCode,State=State,Qualification=Qualification,Course=Course,Purpose=Purpose,arrival_year=arrival_year,leaving_year=leaving_year,Duration=Duration,room_no=room_no.upper(),recommend=recommend)
        reg.save()
    stud=Student.objects.all()
    return render(request,'register_student.html',{'stu':stud,'reg_no':reg_no})

def display_student(request):
    if request.method=="POST":
        yr1=request.POST.get('srchyr')
        data=Student.objects.filter(arrival_year__lte=yr1,leaving_year__gte=yr1)
        stdata=Student.objects.filter(arrival_year__lte=yr1,leaving_year__gte=yr1).count()
        stctrh1=Student.objects.filter(room_no='H1',arrival_year__lte=yr1,leaving_year__gte=yr1).count()
        stctrh2=Student.objects.filter(room_no='H2',arrival_year__lte=yr1,leaving_year__gte=yr1).count()
        stctrh3=Student.objects.filter(room_no='H3',arrival_year__lte=yr1,leaving_year__gte=yr1).count()
        stctrh4=Student.objects.filter(room_no='H4',arrival_year__lte=yr1,leaving_year__gte=yr1).count()
        stctrh5=Student.objects.filter(room_no='H5',arrival_year__lte=yr1,leaving_year__gte=yr1).count()
        return render(request, 'display_student.html', {'stud':data,'stud_ctr':stdata,'stud_h1':stctrh1,'stud_h2':stctrh2,
                                                    'stud_h3':stctrh3,'stud_h4':stctrh4,'stud_h5':stctrh5})

    data=Student.objects.all()
    stdata=Student.objects.all().count()
    stctrh1=Student.objects.filter(room_no='H1').count()
    stctrh2=Student.objects.filter(room_no='H2').count()
    stctrh3=Student.objects.filter(room_no='H3').count()
    stctrh4=Student.objects.filter(room_no='H4').count()
    stctrh5=Student.objects.filter(room_no='H5').count()
    al_ctr = Alumni.objects.all().count()
    return render(request, 'display_student.html', {'stud':data,'stud_ctr':stdata,'stud_h1':stctrh1,'stud_h2':stctrh2,
                                                'stud_h3':stctrh3,'stud_h4':stctrh4,'stud_h5':stctrh5,'alumni_count':al_ctr})

def move(request,id):
    if request.method=="POST":
        alstdata = Student.objects.get(pk=id)
        reg_id=alstdata.reg_id
        fname=alstdata.fname
        mname=alstdata.mname
        lname=alstdata.lname
        email=alstdata.email
        mobile_number=alstdata.mobile_number
        father_occupation=alstdata.father_occupation
        locl_grd=alstdata.locl_grd
        locl_grd_add=alstdata.locl_grd_add
        Institute=alstdata.Institute
        gender=alstdata.gender
        Bdate = alstdata.Bdate
        Address=alstdata.Address
        City=alstdata.City
        PinCode=alstdata.PinCode
        State=alstdata.State
        Qualification=alstdata.Qualification
        Course=alstdata.Course
        Purpose=alstdata.Purpose
        arrival_year=alstdata.arrival_year
        leaving_year=alstdata.leaving_year
        Duration=leaving_year-arrival_year
        room_no=alstdata.room_no
        recommend=alstdata.recommend

        alumni = Alumni(reg_id=reg_id,fname=fname,mname=mname,lname=lname,email=email,mobile_number=mobile_number,father_occupation=father_occupation,locl_grd=locl_grd,locl_grd_add=locl_grd_add,Institute=Institute,gender=gender,Bdate=Bdate,Address=Address,City=City,PinCode=PinCode,State=State,Qualification=Qualification,Course=Course,Purpose=Purpose,arrival_year=arrival_year,leaving_year=leaving_year,Duration=Duration,room_no=room_no,recommend=recommend)
        alumni.save()
        alstdata.delete()
        return redirect('/display_student')

def alumni(request):
    if request.method=="POST":
        yr1=request.POST.get('alsrchyr')
        aldata=Alumni.objects.filter(arrival_year__lte=yr1,leaving_year__gte=yr1)
        al_ctr=Alumni.objects.filter(arrival_year__lte=yr1,leaving_year__gte=yr1).count()
        return render(request, 'alumni.html', {'info':aldata,'alumni_count':al_ctr})

    st_ctr = Student.objects.all().count()
    stctrh1=Student.objects.filter(room_no='H1').count()
    stctrh2=Student.objects.filter(room_no='H2').count()
    stctrh3=Student.objects.filter(room_no='H3').count()
    stctrh4=Student.objects.filter(room_no='H4').count()
    stctrh5=Student.objects.filter(room_no='H5').count()
    aldata = Alumni.objects.all()
    al_ctr = Alumni.objects.all().count()
    return render(request,'alumni.html',{"info":aldata,"alumni_count":al_ctr,"stud_ctr":st_ctr,
                                         'stud_h1':stctrh1,'stud_h2':stctrh2,'stud_h3':stctrh3,
                                         'stud_h4':stctrh4,'stud_h5':stctrh5})

def open_student(request,rno):
    stdatanew=Student.objects.filter(room_no=rno)
    return render(request,"open_student.html",{"newdata":stdatanew,"room":rno})


def register_guest(request):
    regno=1001 if Guest.objects.count() == 0 else Guest.objects.aggregate(max=Max('reg_number'))["max"]+1
    if request.method =='POST':
        roomno=request.POST.get('room_no')
        ctr=Guest.objects.filter(roomno=roomno).count()
        if(ctr > 3):
            return render(request,'register_guest.html',{'error':True,'rno':roomno})

        f_name=request.POST.get('FirstName')
        l_name=request.POST.get('LastName')
        e_mail=request.POST.get('EmailID')
        mobile_no=request.POST.get('MobileNumber')
        Gender=request.POST.get('Gender')
        institute_name=request.POST.get('Institute')
        perm_address=request.POST.get('Address')
        city=request.POST.get('City')
        pinCode=request.POST.get('PinCode')
        state=request.POST.get('State')
        workshop=request.POST.get('Workshop')
        purpose=request.POST.get('Purpose')
        arrival_date=request.POST.get('arrival_date')
        leaving_date=request.POST.get('leaving_date')
        duration = ((date.fromisoformat(leaving_date)) - (date.fromisoformat(arrival_date))).days
        regi=Guest(reg_number=regno,f_name=f_name,l_name=l_name,e_mail=e_mail,mobile_no=mobile_no,Gender=Gender,institute_name=institute_name,perm_address=perm_address,city=city,pinCode=pinCode,state=state,workshop=workshop,purpose=purpose,arrival_date=arrival_date,leaving_date=leaving_date,duration=duration,roomno=roomno.upper())
        regi.save()
    guestt=Guest.objects.all()
    return render(request,'register_guest.html',{'gue':guestt,'regno':regno})
 
def display_guest(request):
    if request.method=="POST":
        yr2=request.POST.get('srch_date')
        data=Guest.objects.filter(arrival_date__lte=yr2,leaving_date__gte=yr2)
        gstdata=Guest.objects.filter(arrival_date__lte=yr2,leaving_date__gte=yr2).count()
        gstctrg1=Guest.objects.filter(roomno='G1',arrival_date__lte=yr2,leaving_date__gte=yr2).count()
        gstctrg2=Guest.objects.filter(roomno='G2',arrival_date__lte=yr2,leaving_date__gte=yr2).count()
        gstctrg3=Guest.objects.filter(roomno='G3',arrival_date__lte=yr2,leaving_date__gte=yr2).count()
        gstctrg4=Guest.objects.filter(roomno='G4',arrival_date__lte=yr2,leaving_date__gte=yr2).count()
        gstctrg5=Guest.objects.filter(roomno='G5',arrival_date__lte=yr2,leaving_date__gte=yr2).count()
        return render(request, 'display_guest.html', {'guestt':data,'guestt_ctr':gstdata,'guestt_g1':gstctrg1,'guestt_g2':gstctrg2,
                                                'guestt_g3':gstctrg3,'guestt_g4':gstctrg4,'guestt_g5':gstctrg5})

    data=Guest.objects.all()
    gstdata=Guest.objects.all().count()
    gstctrg1=Guest.objects.filter(roomno='G1').count()
    gstctrg2=Guest.objects.filter(roomno='G2').count()
    gstctrg3=Guest.objects.filter(roomno='G3').count()
    gstctrg4=Guest.objects.filter(roomno='G4').count()
    gstctrg5=Guest.objects.filter(roomno='G5').count()
    return render(request, 'display_guest.html', {'guestt':data,'guestt_ctr':gstdata,'guestt_g1':gstctrg1,'guestt_g2':gstctrg2,
                                                'guestt_g3':gstctrg3,'guestt_g4':gstctrg4,'guestt_g5':gstctrg5})

def move_guest(request,id):
    if request.method=="POST":
        algstdata = Guest.objects.get(pk=id)
        reg_number=algstdata.reg_number
        f_name=algstdata.f_name
        l_name=algstdata.l_name
        e_mail=algstdata.e_mail
        mobile_no=algstdata.mobile_no
        Gender=algstdata.Gender
        institute_name=algstdata.institute_name
        perm_address=algstdata.perm_address
        city=algstdata.city
        pinCode=algstdata.pinCode
        state=algstdata.state
        workshop=algstdata.workshop
        purpose=algstdata.purpose
        arrival_date=algstdata.arrival_date
        leaving_date=algstdata.leaving_date
        duration=algstdata.duration
        roomno=algstdata.roomno
        pastguest = PastGuest(reg_number=reg_number,f_name=f_name,l_name=l_name,e_mail=e_mail,mobile_no=mobile_no,Gender=Gender,institute_name=institute_name,perm_address=perm_address,city=city,pinCode=pinCode,state=state,workshop=workshop,purpose=purpose,arrival_date=arrival_date,leaving_date=leaving_date,duration=duration,roomno=roomno)
        pastguest.save()
        algstdata.delete()
        return redirect('/display_guest')


def past_guest(request):
    if request.method=="POST":
        date1=date.fromisoformat(request.POST.get('srchdate'))
        pastgstdata=PastGuest.objects.filter(arrival_date__lte=date1,leaving_date__gte=date1)
        pastgst_ctr=PastGuest.objects.filter(arrival_date__lte=date1,leaving_date__gte=date1).count() 
        return render(request,'past_guest.html',{'reqdata':pastgstdata,"guest_count":pastgst_ctr})
        
    pastgstdata = PastGuest.objects.all()
    pastgst_ctr = PastGuest.objects.all().count()
    return render(request,'past_guest.html',{"reqdata":pastgstdata,"guest_count":pastgst_ctr})

def open_guest(request,Rno):
    gstdatanew=Guest.objects.filter(roomno=Rno)
    return render(request,"open_guest.html",{"newdata":gstdatanew,"room":Rno})

def register_kits(request):
    H_kit=HospitalityKit.objects.all()
    return render(request,'register_kits.html',{'H_kit':H_kit})

def add(request):
    if request.method =='POST':
        room_no=request.POST.get('room_no')
        blankets=request.POST.get('blankets')
        pillows=request.POST.get('pillows')
        kettle=request.POST.get('kettle')
        toothpaste=request.POST.get('toothpaste')
        table=request.POST.get('table')
        chairs=request.POST.get('chairs')
        soap=request.POST.get('soap')

        H_kit=HospitalityKit(room_no=room_no,blankets=blankets,pillows=pillows,kettle=kettle,toothpaste=toothpaste,table=table,chairs=chairs,soap=soap)
        H_kit.save()  
    
    return redirect('/register_kits')

def addRoom(request):
    if request.method =='POST':
        room_no=request.POST.get('room_no')
        Room =Create_Room(room_no=room_no)
    
    return redirect('hostel')

def edit(request):
    H_kit=HospitalityKit.objects.all()
    return redirect(request,'register_kits.html',{'kit':H_kit})

def update(request,id):
    if request.method=="POST":
        room_no=request.POST.get('room_no')
        blankets=request.POST.get('blankets')
        pillows=request.POST.get('pillows')
        kettle=request. POST.get('kettle')
        toothpaste=request.POST.get('toothpaste')
        table=request.POST.get('table')
        chairs=request.POST.get('chairs')
        soap=request.POST.get('soap')

        H_kit=HospitalityKit(id=id,room_no=room_no,blankets=blankets,pillows=pillows,kettle=kettle,toothpaste=toothpaste,table=table,chairs=chairs,soap=soap)
        H_kit.save()
    return redirect('/register_kits')

def delete(request,id):
    H_kit=HospitalityKit.objects.filter(id=id)
    H_kit.delete()
    return redirect('/register_kits')

def edit_st(request):
    stud=Student.objects.all()
    return redirect(request,'display_student.html',{'stud':stud})

def stu_print(request,id):
    obj = get_object_or_404(Student, pk=id)
    return render(request, 'stu_print.html', {'k': obj})

def pdf_stud(request,id):
    obj = get_object_or_404(Student, pk=id)
    template_path = 'pdf_stud.html'
    context = {'k': obj}
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="student_form.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def guest_print(request,id):
    obj = get_object_or_404(Guest, pk=id)
    return render(request, 'guest_print.html', {'m': obj})

def pdf_guest(request,id):
    obj = get_object_or_404(Guest, pk=id)
    template_path = 'pdf_guest.html'
    context = {'m': obj}
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="guest_form.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def update_st(request,id):
    if request.method=="POST":
        reg_id=request.POST.get('reg_id')
        fname=request.POST.get('FirstName')
        mname=request.POST.get('MiddleName')
        lname=request.POST.get('LastName')
        email=request.POST.get('EmailID')
        mobile_number=request.POST.get('MobileNumber')
        gender=request.POST.get('Gender')
        Bdate = request.POST.get('birthdate')
        Address=request.POST.get('Address')
        City=request.POST.get('City')
        PinCode=request.POST.get('PinCode')
        State=request.POST.get('State')
        Qualification=request.POST.get('Qualification')
        Course=request.POST.get('Course')
        Purpose=request.POST.get('Purpose')
        arrival_year=request.POST.get('arrival_year')
        leaving_year=request.POST.get('leaving_year')
        Duration=int(leaving_year)-int(arrival_year)
        room_no=request.POST.get('room_no')
        
        stud=Student(id=id,reg_id=reg_id,fname=fname,mname=mname,lname=lname,email=email,mobile_number=mobile_number,
                            gender=gender,Bdate=Bdate,Address=Address,City=City,PinCode=PinCode,State=State,
                            Qualification=Qualification,Course=Course,Purpose=Purpose,arrival_year=arrival_year,
                            leaving_year=leaving_year,Duration=Duration,room_no=room_no)
        stud.save()
    return redirect('/display_student')

def edit_guest(request):
    data=Guest.objects.all()
    return redirect(request,'display_guest.html',{'guestt':data})

def update_guest(request,id):
    if request.method=="POST":
        reg_id=request.POST.get('reg_number')
        fname=request.POST.get('FirstName')
        lname=request.POST.get('LastName')
        email=request.POST.get('EmailID')
        mobile_number=request.POST.get('MobileNumber')
        gender=request.POST.get('Gender')
        institute=request.POST.get('Institute')
        Address=request.POST.get('Address')
        City=request.POST.get('city')
        State=request.POST.get('state')
        PinCode=request.POST.get('pinCode')
        workshop=request.POST.get('workshop')
        Purpose=request.POST.get('purpose')
        arrival_date=request.POST.get('arrival_date')
        leaving_date=request.POST.get('leaving_date')
        duration = ((date.fromisoformat(leaving_date)) - (date.fromisoformat(arrival_date))).days
        room_no=request.POST.get('room_no')

        guest_data=Guest(id=id,reg_number=reg_id,f_name=fname,l_name=lname,e_mail=email,mobile_no=mobile_number,
                            Gender=gender,institute_name=institute,perm_address=Address,city=City,state=State,pinCode=PinCode,
                            workshop=workshop,purpose=Purpose,arrival_date=arrival_date,leaving_date=leaving_date,duration=duration,roomno=room_no)
        guest_data.save()
    return redirect('/display_guest')


def guest_search(request):
    if request.method=="POST":
        date1=date.fromisoformat(request.POST.get('adate'))
        date2=date.fromisoformat(request.POST.get('ldate'))
        gstdata=PastGuest.objects.filter(arrival_date__gte=date1,leaving_date__lte=date2)
    return render(request,'guest_search.html',{'gstdata':gstdata})

