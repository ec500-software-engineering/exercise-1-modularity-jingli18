# EC500_Spring19

Storage Module
================
**The storage module contains four basic functions**

  * insert: obtain json from input module and store patient's data

  * delete: input patient's id(number) in order to complete the deletion. 

  * Update: update patient's data according to the id(number) and json. 

  * Search: input patient's id(number) in order to search the current data of the patient. 

**Table elements**

  * {PatientID, name, gender, age, blood pressure, pressureRange, oxygen, oxRange, pulse, pulseRange, time}

Implementation
================
  * We have two MongoDB implementations, storage.py by Xiangkun Ye and storage_mongo.py by Zhangyu Wan, they basically have the same function, you could choose each one to use.

The table inside MongoDb will look like:
{'PatientID': '1234', 'name': 'John', 'gender': 'Male', 'age': '30', 'pulse': '90', 'pulseRange': {'lower': '50', 'upper': '120'}, 'bloodPressure': '80', 'pressureRange': {'lower': '30', 'upper': '100'}, 'bloodOx': '83', 'oxRange': {'lower': '60', 'upper': '90'}, 'time': '12:05:20pm-18/01/2019'}

  * We have one MySQLDB implementation, storage_mysqldb.py by Alex Jeffrey Lin, same funtionalities which creates a table for inserting values, searching patient data, updating patient info and deleting patient data.  

The table inside MySQLDB will look like: 

(('1234', 'John', 'Male', 30, '12-Feb-19', '80', '83', '90'),) #obtained values

id: 1234, patientName: John, gender: Male, age: 30, time: 12-Feb-19, blood_pressure: 80, blood_oxygen: 83, pulse: 90
