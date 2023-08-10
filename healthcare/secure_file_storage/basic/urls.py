from django.urls import path, re_path
from basic import views

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('add_staff/', views.add_staff, name='add_staff'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('forget', views.forget, name='forget'),
    path('forgetpass', views.forgetpass, name='forgetpass'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('add_doctors/', views.add_doctor, name='add_doctor'),
    path('upload_file/<int:id>', views.upload_file, name='upload_file'),
    path('records/', views.records, name='records'),
    path('viewprofile/', views.viewprofile, name='viewprofile'),
    path('staffprofile/', views.staffprofile, name='staffprofile'),
    path('viewstaffuser/', views.viewstaffuser, name='viewstaffuser'),
    path('viewdoctorss/', views.viewdoctorss, name='viewdoctorss'),
    path('viewpaymentss/', views.viewpaymentss, name='viewpaymentss'),

    path('patientrecord/', views.patientrecord, name='patientrecord'),
    path('viewdoctorrecord/', views.viewdoctorrecord, name='viewdoctorrecord'),
    path('doctorprofile/', views.doctorprofile, name='doctorprofile'),
    path('viewslot/', views.viewslot, name='viewslot'),
    path('finalstaff/', views.finalstaff, name='finalstaff'),

    path('slots/', views.slots, name='slots'),
    path('pay/userpayment', views.userpayment, name='userpayment'),
    path('viewappointment/', views.viewappointment, name='viewappointment'),
    path('slots/addslot', views.addslot, name='addslot'),
    path('appoints/<int:id>', views.appoints, name='appoints'),
    path('pay/<int:id>', views.pay, name='pay'),
    path('addpres/<int:id>', views.addpres, name='addpres'),
    path('addpress', views.addpress, name='addpress'),
    path('appoints/addapoint', views.addapoint, name='addapoint'),
    path('emaill/', views.emaill, name='emaill'),

    path('add_patient/', views.add_patient, name='add_patient'),
    path('home/', views.home, name='home'),
    re_path(r'^patients_downloads/(?P<id>\d+)/$', views.patients_downloads, name='patients_downloads'),
    re_path(r'^download/(?P<id>\d+)/$', views.download, name='download'),
    re_path(r'^patient_records/(?P<id>\d+)/$', views.patient_records, name='patient_records'),
]