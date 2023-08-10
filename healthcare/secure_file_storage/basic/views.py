from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import Doctor, PatientRecord, Patient
from django.http import FileResponse
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from basic import aes
from datetime import datetime
import time
from basic.models import *
import random
from urllib.parse import urlencode
import pycurl
from django.db.models import Q
import certifi
import pycurl
import os
from django.core.mail import send_mail
from .import blockchain  
import pycurl
from urllib.parse import urlencode
# Create your views here.
def sends_mail(mail,msg):

	crl = pycurl.Curl()
	crl.setopt(crl.URL, 'https://alc-training.in/gateway.php')
	data = {'email': mail,'msg':msg}
	pf = urlencode(data)

	# Sets request method to POST,
	# Content-Type header to application/x-www-form-urlencoded
	# and data to send in request body.
	crl.setopt(crl.POSTFIELDS, pf)
	crl.perform()
	crl.close()
        
def index(request):
    return render(request, 'index.html', {})


def admin_home(request):
    return render(request, 'adminhome.html', {})

def add_staff(request):
    return render(request, 'add_staff.html', {})

def viewslot(request):
    user=slot.objects.all()

    return render(request,'viewslot.html',{'res':user})
def viewappointment(request):
    user=appoint.objects.filter(dname=request.session['dname'],status='pending')

    return render(request,'viewapp.html',{'res':user})

def forget(request):
    return render(request, 'forget.html')

def forgetpass(request):
    email = request.POST.get('email')
   
    if Patient.objects.filter(email=email).exists():
        patient = Patient.objects.get(email=email)
        b = patient.email
        password = patient.password
        message = f"Your password is {password}."
        sends_mail(b,message )
        return redirect(index)
    

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    aes.file_exist()
    if username == 'admin' and password == 'admin':
        request.session['username'] = username
        request.session['user'] = 'admin'
        join = PatientRecord.objects.select_related('patient')
        return render(request, 'adminhome.html')
    elif Doctor.objects.filter(username=username, password=password).exists():
        user=Doctor.objects.get(username=username, password=password)
        
        request.session['did'] = user.id
        request.session['dname'] = username
        request.session['user'] = 'doctor'
        doctor = Doctor.objects.get(username=username)
        join = PatientRecord.objects.select_related('patient').filter(doctor_id=doctor.id)
        return render(request, 'doctor_view_patients_record.html', {'data': join})
    elif Patient.objects.filter(username=username, password=password).exists():
        userdetails=Patient.objects.get(username=username, password=password)
        request.session['uid'] = userdetails.id
        request.session['username'] = username
        request.session['user'] = 'patient'

        patient = Patient.objects.get(username=username)
        records = PatientRecord.objects.filter(patient_id=patient.id)
        return render(request, 'patients_medical_records.html', {'data': records})
    elif staff.objects.filter(username=username, password=password).exists():
        userdetails=staff.objects.get(username=username, password=password)
        request.session['sid'] = userdetails.id
        request.session['username'] = username
        request.session['user'] = 'staff'

       
        return render(request, 'staffhome.html')
         
        
        
    else:
        return render(request, 'index.html', {'status': 'failed'})

def patients_downloads(request, id):
    print("++++++++++++++++++++++", id)
    records = PatientRecord.objects.select_related('patient').get(id=id)
    username = records.patient.username
    print("username",username)
    if request.method == 'POST':
        request_key = request.POST.get('key')
        records = PatientRecord.objects.select_related('patient').get(id=id)
        username = records.patient.username
        patient = Patient.objects.get(username=username)
        if request_key == patient.key:
            patient = Patient.objects.get(username=username)
            records = PatientRecord.objects.filter(patient_id=patient.id)
            # patient = Patient.objects.get(username=username)
            # records = PatientRecord.objects.filter(patient_id=patient.id)
            # rec_id = records.id

            obj = PatientRecord.objects.get(id=id)
            patient_path = 'basic/static/patients_record'.split('/')
            patient_path_combined = patient_path[0] + os.sep + patient_path[1] + os.sep + patient_path[2]
            file_path = patient_path_combined.format(obj.file)
            fetch_patients = PatientRecord.objects.select_related('patient').get(id=id)
            file = aes.decrypt(obj.file, fetch_patients.patient.key)
            if os.path.exists(file):
                with open(file, 'rb') as fh:
                    response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                    response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file)
                    return response
            raise Http404
            return render(request, 'patients_medical_records_downloads.html', {'data': records})
        else:
            return render(request, 'patients_home.html', {'id':id,'status': 'You have Entered the wrong key'})
    else:
        print("passing id", id)
        return render(request, 'patients_home.html', {'id':id,'status': ''})

def logout(request):
    if 'username' in request.session:
        request.session.flush()
        return redirect(index)
    else:
        return redirect(index)

def patient_records(request, id):
    records = PatientRecord.objects.select_related('patient').get(id=id)
    username = records.patient.username
    patient = Patient.objects.get(username=username)
    records = PatientRecord.objects.filter(patient_id=patient.id)
    return render(request, 'patients_medical_records.html', {'data': records})

def records(request):
    fetch_patients = PatientRecord.objects.select_related('patient')
    return render(request, 'admin_records.html', {'data': fetch_patients})
    

def add_doctor(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        department = request.POST.get('department')
        gender = request.POST.get('gender')
        if Doctor.objects.filter(username=username).exists():
            return render(request, 'add_doctors.html', {'status': 'exist'})
        else:
            doctor_object = Doctor.objects.create(name=name, email=email, username=username, password=password,
                                                  address=address,
                                                  phone=phone, department=department, gender=gender)
            if doctor_object:
                return render(request, 'add_doctors.html', {'status': 'success'})
            else:
                return render(request, 'add_doctors.html', {'status': 'failed'})
    else:
        return render(request, 'add_doctors.html', {})
def finalstaff(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        department = request.POST.get('department')
        gender = request.POST.get('gender')
        if staff.objects.filter(username=username).exists():
            return render(request, 'add_staff.html', {'status': 'exist'})
        else:
            doctor_object = staff.objects.create(name=name, email=email, username=username, password=password,
                                                  address=address,
                                                  phone=phone,gender=gender)
            if doctor_object:
                return render(request, 'add_staff.html', {'status': 'success'})
            else:
                return render(request, 'add_staff.html', {'status': 'failed'})
    else:
        return render(request, 'add_staff.html', {})


def add_patient(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    username = request.POST.get('username')
    password = request.POST.get('password')
    gender = request.POST.get('gender')
    age = request.POST.get('age')
    rand_num = random.randrange(1000, 10000)

    key = rand_num
    phone = request.POST.get('phone')
   
    if Patient.objects.filter(username=username, email=email).exists():
        return render(request, 'index.html', {'message': 'User Exists'})
    else:
        
        patient = Patient.objects.create(name=name,email=email, username=username, password=password,gender=gender, age=age, phone=phone, key=key)
        msg='Your Key is '+str(key)
        crl = pycurl.Curl()
        crl.setopt(pycurl.CAINFO, certifi.where())
        crl.setopt(crl.URL, 'https://alc-training.in/gateway.php')
        data = {'email': email, 'msg':msg}
        pf = urlencode(data)

                    # Sets request method to POST,
                    # Content-Type header to application/x-www-form-urlencoded
                    # and data to send in request body.
        crl.setopt(crl.POSTFIELDS, pf)
        crl.perform()
        crl.close()
        return render(request, 'index.html', {'message': 'Successfully Register'})
        

def upload_file(request,id):
    if request.method == 'POST':
        patient_id1 = request.POST.get('patientt')
        sell=Patient.objects.get(username=patient_id1)
        patient_id=str(sell.id)
        doctor_id = request.POST.get('doctor')
        file = request.FILES["file"]
        fs = FileSystemStorage("basic/static/patients_record")
        time.sleep(1)
        now = datetime.today()
        r = now.strftime("%m%d%Y%H%M%S")
        split = str(file).split('.')
        filename = split[0]+patient_id+r+'.'+split[1]
        fs.save(filename, file)
        password = Patient.objects.get(id=patient_id).key
        saved_file_name = aes.encrypt(filename, password)

        doctor = Doctor.objects.all()
        patient =Patient.objects.all()
        

        patient_object = PatientRecord.objects.create(patient_id=patient_id, doctor_id=doctor_id, file=saved_file_name)
        if patient_object:
            return render(request, 'upload_record.html', {'status': 'success', 'doctor': doctor, 'patient': patient})
        else:
            return render(request, 'upload_record.html', {'status': 'failed', 'doctor': doctor, 'patient': patient})
    else:
        doctor = request.session['did']

        patient = appoint.objects.get(id=id)
        
        return render(request, 'upload_record.html', {'doctor': doctor, 'patient': patient})


def download(request, id):
    obj = PatientRecord.objects.get(id=id)
    print(obj)
    patient_path = 'basic/static/patients_record'.split('/')
    print(patient_path)

    patient_path_combined = patient_path[0] + os.sep + patient_path[1] + os.sep + patient_path[2]
    print(patient_path_combined)

    file_path = patient_path_combined.format(obj.file)
    print(file_path)

    fetch_patients = PatientRecord.objects.select_related('patient').get(id=id)
    print(fetch_patients)

    file = aes.decrypt(obj.file, fetch_patients.patient.key)
    print(file)

    if os.path.exists(file):
        with open(file, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file)
            return response
    raise Http404

def home(request):
    if request.session['user'] == 'admin':
        username = request.session['username']
        join = PatientRecord.objects.select_related('patient')
        return render(request, 'adminhome.html')
    elif request.session['user'] == 'doctor':
        username = request.session['username']
        doctor = Doctor.objects.get(username=username)
        join = PatientRecord.objects.select_related('patient').filter(doctor_id=doctor.id)
        return render(request, 'doctor_view_patients_record.html', {'data': join})
    elif request.session['user'] == 'patient':
        username = request.session['username']
        patient = Patient.objects.get(username=username)
        records = PatientRecord.objects.filter(patient_id=patient.id)
        return render(request, 'patients_medical_records.html', {'data': records})
    else:
        return render(request, 'index.html',{})
        
        
        

def viewprofile(request):
    if request.session.has_key('username'):
        temp=request.session['username']
        users = Patient.objects.get(username=request.session['username'])
        # us=[]
        # us['id']=user.id
        # email= user.email

        return render(request, 'profile.html',{'result': users})
        
def staffprofile(request):
    if request.session.has_key('sid'):
        temp=request.session['sid']
        users = staff.objects.get(id=request.session['sid'])
        # us=[]
        # us['id']=user.id
        # email= user.email

        return render(request, 'staffprofile.html',{'result': users})
       
def viewstaffuser(request):
    users = appoint.objects.all()
        # us=[]
        # us['id']=user.id
        # email= user.email

    return render(request, 'viewuser.html',{'result': users})
        
def viewdoctorss(request):
    users = Doctor.objects.all()
        # us=[]
        # us['id']=user.id
        # email= user.email

    return render(request, 'viewdoctor.html',{'result': users})
     
def viewpaymentss(request):
    users = payment.objects.all()
        # us=[]
        # us['id']=user.id
        # email= user.email

    return render(request, 'viewpayments.html',{'result': users})
        

def patientrecord(request):
    if request.session.has_key('username'):
        temp=request.session['username']
        uid=request.session['uid']
        user = Patient.objects.get(username=request.session['username'])
        a=user.id
        print(a)
        records = PatientRecord.objects.filter(patient_id=user.id)
        # us=[]
        # us['id']=user.id
        # email= user.email
        sel=appoint.objects.filter(Q(status='approved') | Q(status='paid'),pname=temp)
        return render(request, 'patientrecord.html',{'data': records,'result':sel})
        
        
def viewdoctorrecord(request):
    if request.session.has_key('dname'):
        temp=request.session['dname']
        user = Doctor.objects.get(username=request.session['dname'])
        a=user.id
        print(a)
        records = PatientRecord.objects.filter(doctor_id=user.id)
        # us=[]
        # us['id']=user.id
        # email= user.email
        sel=payment.objects.filter(dname=temp)
        return render(request, 'doctorrecord.html',{'data': records,'result':sel})
        
        
def doctorprofile(request):
    if request.session.has_key('dname'):
        temp=request.session['dname']
        users = Doctor.objects.get(username=request.session['dname'])
        # us=[]
        # us['id']=user.id
        # email= user.email

        return render(request, 'doctorprofile.html',{'result': users})
        
        
        
def slots(request):
    if request.session.has_key('dname'):
        temp=request.session['dname']
        # us=[]
        # us['id']=user.id
        # email= user.email

        return render(request, 'slot.html',{'result': temp})
        
        

def addslot(request):
    if request.method == 'POST':
        a = request.POST.get('dname')
        b = request.POST.get('starttime')
        c = request.POST.get('endtime')
        d = request.POST.get('date')
        
        user = slot(dname=a,starttime=b,endtime=c, date=d)
        user.save()                                   
        return render(request,'slot.html')


    
def appoints(request,id):
    users=slot.objects.get(id=id)
    temp=request.session['username']
    return render(request, 'appoint.html',{'res': users,'result':temp})
        
def pay(request,id):
    users=appoint.objects.get(id=id,status='approved')
    return render(request, 'pay.html',{'res': users})
        
def addpres(request,id):
    users=appoint.objects.get(id=id)
    return render(request, 'prescribe.html',{'res': users})
    
    
def addapoint(request):
    if request.method == 'POST':
        a = request.POST.get('dname')
        b = request.POST.get('time')
        c = request.POST.get('symptom')
        d = request.POST.get('date')
        e = request.POST.get('pname')
        f=request.session['uid']
        user = appoint(dname=a,time=b,symptom=c,date=d,pname=e,status='pending')
        user.save()                                   
        return render(request,'appoint.html')
        
def userpayment(request):
    if request.method == 'POST':
        a1 = request.POST.get('dname')
        b1 = request.POST.get('amount')
        c1 = request.POST.get('cardname')
        d1 = request.POST.get('cardnumber')
        e1 = request.POST.get('cvv')
        aid = request.POST.get('aid')
        date = request.POST.get('date')
        sel=appoint.objects.get(id=aid)
        aa=sel.dname
        b = sel.time
        c = sel.symptom
        d = sel.date
        e = sel.pname
        prescribe = sel.prescribe
        amount= sel.amount
        idd = sel.id
        block_chain = blockchain.Block_chain()  
        transaction1 = block_chain.newTransaction(e, d1, e1)  
 
        block_chain.newBlock(10123)  

  
        print("Genesis block: ", block_chain.chain)
        user1 = appoint(amount=amount,dname=aa,time=b,symptom=c,date=d,pname=e,status='paid',prescribe=prescribe,id=idd)
        user1.save()  
        user = payment(dname=a1,amount=b1,cardname=c1,date=date,pname=e,cardnumber=d1,cvv=e1)
        user.save()                                   
        return render(request,'pay.html',{'status':'Successfully Paid'})
        
def addpress(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        a = request.POST.get('pres')
        aid= request.POST.get('aid')
        sel=appoint.objects.get(id=aid)
        aa=sel.dname
        b = sel.time
        c = sel.symptom
        d = sel.date
        e = sel.pname
        idd = sel.id
        user = appoint(amount=amount,dname=aa,time=b,symptom=c,date=d,pname=e,status='approved',prescribe=a,id=idd)
        user.save()                                   
        return redirect(viewappointment)
        
        
        
def emaill(request):
    #crl = pycurl.Curl()
    #crl.setopt(crl.URL, 'https://alc-training.in/gateway.php')
    #data = {'email': 'christeenaarjun03@gmail.com', 'msg': 'successfully login'}
    #pf = urlencode(data)

            # Sets request method to POST,
            # Content-Type header to application/x-www-form-urlencoded
            # and data to send in request body.
    #crl.setopt(crl.POSTFIELDS, pf)
    #crl.perform()
    #crl.close()
    email="gettoanish@gmail.com"
    msg="8888"
    return redirect('https://alc-training.in/gateway.php?email='+email+'&msg='+msg)
    #return redirect('https://alc-training.in/gateway.php?email=christeenaarjun03@gmail.com&msg=key')

