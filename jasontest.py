# Copyright 2019 Jing Li jingli18@bu.edu

#!/usr/bin/python
import json
import os

# patient_dic = {'blood_pressure':120, 'blood_oxgen':12, 'heart_rate':80}
class Patient_output():
    def __init__(self):
        self.PID = 0
        self.patient_dir = os.getcwd()
        print("*********Welcome to Patient Moniter System**********")

    def readjson(self, data):        
        #with open(json_dir + "\\patient.json","r") as read:
        self.new_patient_dic = json.loads(data)
        #print(new_patient_dic)
        print("Patient Data Read!")

    def outprint(self,key):
        output = self.new_patient_dic[key]
        print(output)

    def control(self):
        key = input("Enter the date you want to check: (bloodPressure, pulse, bloodOx, alert_message)")
        if key in ["bloodPressure", "pulse", "bloodOx", "alert_message"] :
            self.outprint(key)
        elif key == 'c':
            return 0
        else:
            print("Please input the right keyword(bloodPressure, pulse, bloodOx, alert_message")
        self.control()