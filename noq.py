import threading
from queue import Queue
import time
import random
import input_module
import alertt
import storage
import json

# generate data in random time
def generate_data(q, q_alert, q_data):
	print("======****** Welcome to Use Patient Monitor ******======")
	print("========================================================")
	print("***************** Copyright Jing Li ********************")
	print("========================================================")
	print("=============", time.ctime(time.time()), "===========")
	while 1:
		times = random.randint(4,7)
		patientData = input_module.genSensorData()
		patientInfo = input_module.genPatientInfo()
		alert_mes = alertt.alertCheck(patientData)
		#print(patientInfo)
		storage.insert(patientInfo, patientData)

		
		q.put(patientInfo)
		print('... ...Waiting for data to be sent to Info... ...\n')
	

		
		q_data.put(patientData)
		print("... ...Waiting for data to be sent to display... ...\n")


		q_alert.put(alert_mes)
		print("... ...Waiting for alert check... ...\n")



		time.sleep(times)
	

# every 5 seconds print the patient information
def print_info(q):
	n = 0
	while 1:
		dataIn = q.get()
		print("Info has got the patient information!\n")
		q.task_done()
		if n%5==0:
			print(dataIn)
			n = 0
		n += 1

def checkAlert(q_alert):

	while 1:
		alertmes = q_alert.get()
		if alertmes != "":
			print(alertmes)
		else:
			print("No Alert \n")
		q_alert.task_done()

# call output to print the data


def output(q_data):
	while 1:
		data = q_data.get()
		print(data)
		q_data.task_done()
# second thread that print the time
# def print_time(threadName, delay):
# 	count = 0
# 	while count < 20:
		
# 		time.sleep(delay)
# 		count += 1
# 		print ("%s: %s \n" % (threadName, time.ctime(time.time()) ))

# Create two threads

q = Queue()
q_data = Queue()
q_alert = Queue()
t2 = threading.Thread(target=generate_data, args=(q, q_alert, q_data))
t1 = threading.Thread(target=print_info, args=(q,))
t3 = threading.Thread(target=output, args=(q_data,))
t4 = threading.Thread(target=checkAlert, args=(q_alert,))

t1.start()
t2.start()
t3.start()
t4.start()
q.join()
q_alert.join()
q_data.join()