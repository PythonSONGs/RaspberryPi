import RPi.GPIO as GPIO
import time

relayPin = 18
i = 0
GPIO.setmode(BOARD)
GPIO.setup(relayPin,GPIO.OUT)

while 1:
	i = i + 1
	print "Watering...",i
	GPIO.output(relayPin,GPIO.HIGH)
	time.sleep(40)
	GPIO.output(relayPin,GPIO.LOW)
	time.sleep(180)
	GPIO.output(relayPin,GPIO.HIGH)
	time.sleep(40)
	GPIO.output(relayPin,GPIO.LOW)
	time.sleep(180)
	print "Done,Sleeping..."
	time.sleep(3340)
	GPIO.cleanup()

GPIO.cleanup()
