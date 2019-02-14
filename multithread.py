import _thread
import time
import random

class multi_input():

	# generate data in random time
	def generate_data(self):
		times = random.randint(1,5)
		time.sleep(times)
		data = random.randint(30, 100)
		self.inputData(data)
		self.generate_data()

	# call output to print the data
	def inputData(self,data_in):
		self.output(data_in)

	def output(self,data_out):   
	    print(data_out, '\n')

	# second thread that print the time
	def print_time(self,threadName, delay):
		count = 0
		while count < 20:
			if count%5 == 0:
				self.output("Alert!")
			time.sleep(delay)
			count += 1
			print ("%s: %s \n" % (threadName, time.ctime(time.time()) ))

	# Create two threads
	def muti(self):
		try:

		   _thread.start_new_thread(self.print_time, ("Time ", 2, ) )
		   _thread.start_new_thread(self.generate_data, () )
		except:
		   print ("Error: unable to start thread")

		while 1:
		   pass

patient = multi_input()
patient.muti()