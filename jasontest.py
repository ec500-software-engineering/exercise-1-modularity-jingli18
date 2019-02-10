# Copyright 2019 Jing Li jingli18@bu.edu

#!/usr/bin/python
import json
import os

# patient_dic = {'blood_pressure':120, 'blood_oxgen':12, 'heart_rate':80}
class Patient_output():
    def __init__(self):
        self.PID = 0
        self.patient_dir = os.getcwd()

    def readjson(self):        
        with open(json_dir + "\\patient.json","r") as read:
        new_patient_dic = json.load(read)
        print(new_patient_dic)
        print("Json Read!")

    def outprint():
        print(new_patient_dic[self.key])

    def control(self):
        self.key = input("Enter the date you want to check: ")
        if key in new_patient_dic.keys() :
            self.outprint()
        elif key == 'c':
            return 0
        else:
            print("Please input the right keyword('blood_oxgen', 'blood_pressure' or 'heart_rate'")
        thd.Timer(5,self.control).start()

        return 0



    control()