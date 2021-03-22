import picamera 
from time import sleep
import time
import schedule

def camrec():
	#import call

	with picamera.PiCamera() as  camera:
		camera.start_recording("pythonvideo.h264")
		sleep(5)	
		camera.stop_recording()
		 
		
	print('We  are going to convert the video')

	command="MP4Box -add pythonVideo.h264 hdfight.mp4"

	#call( [command] , shell = True)

schedule.every(5).seconds.do(camrec)
a=3
#every 10 s do the camera rec
while a==0:
	schedule.run_pending()
	a-=1
	print('running')
	time.sleep(1)
	

 
