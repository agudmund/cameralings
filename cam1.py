#!/usr/bin/env python

from io import BytesIO
from picamera import PiCamera
from time import sleep
import datetime
import os
import keyboard
import RPi.GPIO as GPIO
import time

camera = PiCamera()

print ("  Press Ctrl & C to Quit")

class Camera:
    
    def __init__(self):
        '''Initial Settings'''
        
        #camera.overlays = '/home/zine.png/
        #camera.quality = (20000000)
        camera.image_effect = "film"
        camera.resolution = (1296,730)
        camera.zoom = ( 0.0, 0.0, 1.0, 1.0)
        camera.framerate = (24)
        camera.exposure_compensation = (0)
        #camera.exposure_mode = 'off'
        #camera.range = "high"
        camera.iso = (100)
        camera.shutter_speed =(48000)
        #camera.digital_gain = (70)
        #camera.awb_mode = 'off'
        #camera.awb_gains = (1.1)
        camera.contrast = (1)
        camera.sharpness = (0)
        camera.saturation = (-10)

        camera.iso=799

        self.resmode = "full"
        self.zoomVal = 0.0
        self.zoomMod = 0.1
        
        
        self.setPath()
        
    def setPath(self):
        '''Target Path to Save Video Towards'''

        rootPath = '/home/pi/Documents/Video/'
        timing = datetime.datetime.now().strftime('%Y-%m-%d%H%M%S')
        ext = '.mjpg'
        #quality ='1'
        
        self.targetPath = '%s%s' % (os.path.join(rootPath,timing),ext)

        return self.targetPath
        
    def record(self):
        '''Actual Recording'''
        
        if not camera.recording:
            camera.start_recording(self.targetPath)
        else:
        	camera.stop_recording()
        	if not camera.preview:
                camera.start_preview()

        return True


    
    def detectKeys(self):
        '''Key Assignments'''
        
        if keyboard.is_pressed("1"):
            camera.iso=100
        if keyboard.is_pressed("t"):
            camera.stop_recording
        if keyboard.is_pressed("4"):
            camera.iso=400
        if keyboard.is_pressed("8"):
            camera.iso=799
        if keyboard.is_pressed("q"):
           camera.stop_preview()
        if keyboard.is_pressed("r"):
            self.record()
        if keyboard.is_pressed("p"):
            if self.resmode == "crop":
                camera.resolution = (1920,1080)
                self.resmode = "full"
            else:
                camera.resolution = (1296,730)
                self.resmode = "crop"
            time.sleep(1)
        if keyboard.is_pressed("x"):
            self.zoomMod = -0.1
            self.zoomVal = self.zoomVal + self.zoomMod
            camera.zoom = ( self.zoomVal, self. zoomVal, 1.0 , 1.0)
            time.sleep(1)
        if keyboard.is_pressed("z"):
            self.zoomMod = 0.1
            self.zoomVal = self.zoomVal + self.zoomMod
            camera.zoom = ( self.zoomVal, self. zoomVal, 1.0 , 1.0)
            time.sleep(1)
        if keyboard.is_pressed("a"):
            if not camera.preview:
                camera.start_preview()

        return True
        
    def run(self):
        '''Runtime'''
        
        self.detectKeys()
              
        return True

if __name__ == '__main__':
    piCam = Camera()
    while True:
      piCam.run()
