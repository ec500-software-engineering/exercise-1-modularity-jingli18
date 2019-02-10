import threading as thd
import time
import random
import os
import json

i = 0
def write():
	# patient_dic = {'blood_pressure':random.randint(90, 120), 'blood_oxgen':random.randint(60, 80), 'heart_rate':random.randint(60, 100)}
	# json_dir = os.getcwd()
	# with open(json_dir + "\\patient" + str(i) +".json","w") as write:
	#     json.dump(patient_dic, write)
	print("Json Loaded!")
	thd.Timer(3,write.start()

write()

		