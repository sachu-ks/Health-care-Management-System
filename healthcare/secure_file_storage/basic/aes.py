import pyAesCrypt
import os
from django.core.files.storage import FileSystemStorage
import shutil

import time

def encrypt(file_name, key):
    patient_path = 'basic/static/patients_record'.split('/')
    patient_path_combined = patient_path[0]+os.sep+patient_path[1]+os.sep+patient_path[2]
    path = os.path.join(patient_path_combined, str(file_name))
    output_file_name = str(file_name)+".aes"
    pyAesCrypt.encryptFile(path, output_file_name, key)
    current_path = os.path.join(output_file_name)
    shutil.move(current_path, "basic/static/patients_record")
    os.remove(path)
    return output_file_name.split('/')[-1]

def decrypt(file_name, key):
    output_format = file_name.split('.')[-2]
    patient_path = 'basic/static/patients_record'.split('/')
    patient_path_combined = patient_path[0] + os.sep + patient_path[1] + os.sep + patient_path[2]
    file_path = os.path.join(patient_path_combined, file_name)
    outfile = "output"+'.'+output_format
    pyAesCrypt.decryptFile(file_path, outfile, key)
    return outfile


def file_exist():
    if os.path.exists('output.txt'):
        os.remove('output.txt')
    else:
        pass
    return 'ok'