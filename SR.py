import numpy as np
import cv2
import pyscreenshot as ImageGrab
from SreenRes import *
import time





def screenRecord():
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	out = cv2.VideoWriter("output.avi",fourcc,cv2.CAP_PROP_FPS,(int(k),int(j)))
	while True:
		img = ImageGrab.grab()
		img_np = np.array(img)
		time.sleep(1)
		frame = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)

		cv2.imshow("screen",frame)
		out.write(frame)
		if cv2.waitKey(1)==27:
			break


	out.release()
	cv2.destroyAllWindows()


screenRecord()