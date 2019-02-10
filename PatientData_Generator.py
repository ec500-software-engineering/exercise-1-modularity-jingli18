# Copyright 2019 Jing Li jingli18@bu.edu

import threading as thd
import time
import random
import os
import json

class Patient_Data:
	def __init__(self):
		self.count = 0
		self.dir = os.getcwd()

	def write(self):
		patient_dic = {
		'blood_pressure':random.randint(90, 120), 
		'blood_oxgen':random.randint(60, 80), 
		'heart_rate':random.randint(60, 100)}
		
		with open(self.dir + "\\patient" + str(self.count) +".json","w") as write:
			json.dump(patient_dic, write)		
		print("Patient" + str(self.count) + "Loaded!")
		self.count += 1
		thd.Timer(3,self.write).start()

P = Patient_Data()		
print(time.time())
P.write()
