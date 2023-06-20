from picamera import PiCamera
import time



camera = PiCamera()
camera.resolution = (1920,1080)
camera.vflip = True
camera_record = False


def Record():
	
	
	camera.start_recording("my_movie.h264")


def stop_Recording():
	camera.stop_recording()
Record()
time.sleep(2)
stop_Recording()
	


