#!/usr/bin/env python
# *-* coding:utf-8 *-*

import os
import cv2
from time import sleep,time

class Capture:
	def __init__(self):
		self.name = 'Recorder'
		self.tmpfile = ''
		self.imageroot = ''
		self.framerate = 1
		self.active = False
		self.readSettings()
		self.cam = self.initCam()

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

	def initCam(self):
		video = cv2.VideoCapture()
		
		# Default the camera to 1080p, it falls back on the max resolution supported.
		video.set(3,1920.0)
		video.set(4,1080.0)
		
		video.open(0)

		return video

	def checkIt(self):
		'''Read the status and default to On in case of failure'''
		with open(self.tmpfile ) as data:
			rez = data.readlines()

		try:
			token = rez[0]
		except IndexError as e:
			token = "1"

		if token=="1":
			return True
		else:
			return False
	
	def record(self):
		'''Captures an image to disk'''

		target = os.path.join(os.getcwd(),self.imageroot,str(time())) 
		os.makedirs(target)

		while True:
			ret, image = self.cam.read()
			cv2.imwrite(os.path.join(target,'name.%s.png'%str(time()) ), image)
			sleep(1/self.framerate)
			if not self.checkIt():
				break

		return True

	def loop(self):
		while True:
			if self.checkIt():
				if not self.active:
					print('I can see the sensor')
					self.active = True
					self.record()
			else:
				if self.active:
					print ('Sensor Appears off')
					self.active = False
				
			sleep(1)

if __name__ == '__main__':
	c = Capture()
	c.loop()
