import RPi.GPIO as GPIO
import time
import numpy as np
import cv2

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(1) # Initialization
rate = 1
inc = 1
cap = cv2.VideoCapture(0)
count = 0
try:
  while True:
    p.ChangeDutyCycle(rate)
    rate = rate + inc
    print(rate)
    if rate == 12:
        inc = -1
    elif rate ==1:
        inc = 1
    time.sleep(0.2)
    ret, frame = cap.read()
    #time.sleep(0.2)
    cv2.imwrite("/home/pi/Desktop/frames/frame%d.jpg" % count, frame)
    count+=1
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
cap.release()
cv2.destroyAllWindows()
#while count<20:
    # Capture frame-by-frame
   # ret, frame = cap.read()

    # Our operations on the frame come here
  #  cv2.imwrite("/home/pi/Desktop/frames/frame%d.jpg" % count, frame)

    # Display the resulting frame
 #   count=count +1

# When everything done, release the capture
#cap.release()
#cv2.