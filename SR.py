import numpy as np
import cv2
import pyscreenshot as ImageGrab
from SreenRes import *
import time
import os

def frametime_checker():
	ti=time.time()
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	out = cv2.VideoWriter("temp.avi",fourcc,cv2.CAP_PROP_FPS,(int(k),int(j)))
	i=0
	while i<5:
		img = ImageGrab.grab()
		img_np = np.array(img)
		frame = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
		out.write(frame)
		i+=1
	tf=time.time()
	out.release()
	os.delete('temp.avi')
	frame_interval = (tf-ti)/5
	framerate=int(1/farme_interval)
	return farmerate




def screenRecord(farmerate):
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	out = cv2.VideoWriter("output.avi",fourcc,framerate,(int(k),int(j)))
	while True:
		img = ImageGrab.grab()
		img_np = np.array(img)
		time.sleep(1)
		frame = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
		out.write(frame)
		if cv2.waitKey(1)==27:
			break
	out.release()
	cv2.destroyAllWindows()


screenRecord(frametime_checker())
