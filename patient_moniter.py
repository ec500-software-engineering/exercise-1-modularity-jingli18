from input import input_module
from storage import storage
from alert import alert_system
import jasontest
import json
#import os

'''
input module
from https://github.com/alexlin0625/EC500_Spring19/tree/input_module
'''

patientData = input_module.readSensorData()
patientInfo = input_module.getPatientInfo()

'''
storage_module
from https://github.com/alexlin0625/EC500_Spring19/tree/storage_module
'''

storage.insert(patientInfo, patientData)

'''
alert_system
from https://github.com/alexlin0625/EC500_Spring19/tree/alert-system
'''

patient_Data, patient_alert = alert_system.alertCheck(patientInfo, patientData)
'''
output_module
from https://github.com/ec500-software-engineering/exercise-1-modularity-jingli18
'''   
#patient1.send_alert_to_UI(patient_alert)

patient_test = jasontest.Patient_output()
patient_test.readjson(patient_Data)
patient_test.control()
print(patient_test.new_patient_dic)
