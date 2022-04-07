import cv2
import numpy as np
import pyautogui
import datetime
import keyboard
import datetime

def recording():
	SCREEN_SIZE = (3440, 1440)
	FRAME_RATE = 30.0
	fourcc = cv2.VideoWriter_fourcc(*"XVID")
	now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
	out = cv2.VideoWriter("screen recorder"+now+".avi", fourcc, FRAME_RATE, (SCREEN_SIZE))
	while not keyboard.is_pressed('K'):
	    st = time.time()  # collect start time
	    img = pyautogui.screenshot()
	    frame = np.array(img)
	    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	    out.write(frame)
	    en = time.time()  # collect end time
	    # calculate time to wait before next frame:
	    delay = max(0, (1 / FRAME_RATE - (en - st)) * 1000)  
	    # if the user clicks q, it exits

	cv2.destroyAllWindows()
	out.release()

recording()

