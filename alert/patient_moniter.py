from input import input_module
from storage import storage
from alert import alert_system
import jasontest
import json
import os

def main():

    '''
    input module
    from https://github.com/alexlin0625/EC500_Spring19/tree/input_module
    '''

    patientData = input.readSensorData()
    patientInfo = input.getPatientInfo()
    input_sendor_data = json.loads(patientData)
    input_patient_data = json.loads(patientInfo)

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

    '''update this table to set pulse = 100: '''
    #storage.update("1234", '17:05:20pm-01/02/2019', 'bloodOx', '90')
    '''search a person with PatientID 1234: '''
    #patient_alert = storage.searchPerson("1234")


if __name__ == "__main__":
    main()