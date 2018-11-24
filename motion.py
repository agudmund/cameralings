#!/usr/bin/env python

import cv2
import numpy
from time import time,sleep


if __name__ == '__main__':
	cam = cv2.VideoCapture()
	cam.open(0)
	last = [0,0,0]
	while True:
		sleep(0.3)
		ret, image = cam.read()
		if (int(numpy.mean(image)) == int(numpy.mean(last))):
			print('static')
			continue
		else:
			print('motion')
		last = image
	cam.release()