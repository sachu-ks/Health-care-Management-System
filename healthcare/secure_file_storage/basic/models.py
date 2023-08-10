from django.db import models


# Create your models here.

class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=130)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=230)
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
class staff(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=130)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=230)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=100)


class Patient(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100, default=None)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=130)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.CharField(max_length=100, default=None)
    key = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)


class PatientRecord(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE)
    file = models.CharField(max_length=200)

class blockchainoutput(models.Model):
    output = models.CharField(max_length=150)
   

class slot(models.Model):
    id = models.AutoField(primary_key=True)
    dname = models.CharField(max_length=200)
    starttime = models.CharField(max_length=200)
    endtime = models.CharField(max_length=200)
    date = models.CharField(max_length=200)

class appoint(models.Model):
    dname = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    symptom = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    pname = models.CharField(max_length=200)
    prescribe = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    amount = models.CharField(max_length=200)


class payment(models.Model):
    dname = models.CharField(max_length=200)
    amount = models.CharField(max_length=200)
    pname = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    cardname = models.CharField(max_length=200)
    cardnumber = models.CharField(max_length=200)
    cvv = models.CharField(max_length=200)

