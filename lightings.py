#!/usr/bin/env python
# *-* coding:utf-8 *-*

import os
import serial
import time
import argparse
import geocoder

parser = argparse.ArgumentParser(description='LDR Sensor')
parser.add_argument('-d','--debug', help='Debug',action="store_true")
args = parser.parse_args()

class Connect:
	def __init__( self, port='COM7' ):
		self.name = 'LDR Connector'
		self.active = False
		self.serial = serial.Serial( port )
		self.tmpfile = ''
		self.location = geocoder.ip("me").latlng
		self.readSettings()
		self.logstart = time.time()
	
	def readSettings(self):
		with open("settings") as data:
			rez = data.readlines()
		for n in rez:
			attribute = n.split()[0]
			value = n.split()[1]
			if value[0].isdigit():
				exec('self.%s = %s' % ( attribute, value ) )
			else:
				exec('self.%s = "%s"' % ( attribute, value ) )
		self.tmpfile = os.path.join(os.getenv("TMP"),self.tmpfile)

	def markIt( self, token ):
		"""Logs activity into a file for other daemons to read"""
		with open( self.tmpfile ,'w') as data:
			data.write( token )

		return True

	def scratchIt(self,text):
		print (text)
		thing = '''function something()
{
    document.getElementById("Ticker").innerText = "NNNTOKENNNN";
    setTimeout(something, 100);

}
'''
		with open('serv/ldrsite/tick/static/thingling.js','w') as data:
			data.write(thing.replace('NNNTOKENNNN',text))

	def debug(self):
		"""Prints out the current LDR voltage information"""
		while True:
			reading = self.serial.readline()
			toString = reading.decode()
			print(toString.rstrip('\n'))

	def logDaylight(self, stamp):
		'''Logs the default light value for the time of day on 60 second intervals'''

		if time.time() - self.logstart>60:
			self.logstart = time.time()
			with open(self.logfile,'a') as data:
				data.write('%s %s %s %s\n'%(self.location[0], self.location[1], time.time(),stamp))


	def loop(self):
		while True:
			reading = self.serial.readline()
			self.logDaylight(reading.decode().replace('\n','').replace('\r',''))
			if int(reading)>200:
				if not self.active:
					self.scratchIt('Light On')
				self.active = True
				self.markIt('1')
			else:
				if self.active:
					self.scratchIt( 'Light Off')
				self.active = False
				self.markIt('0')
		return True

if __name__ == '__main__':
	connect = Connect()
	if args.debug:
		connect.debug()
	else:
		connect.loop()
