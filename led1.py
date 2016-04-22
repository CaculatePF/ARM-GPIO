import RPi.GPIO
import time
RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(14, RPi.GPIO.OUT)
for i in range(0, 10):
	RPi.GPIO.output(14, True)
	time.sleep(2)
	RPi.GPIO.output(14, False)
	time.sleep(2)

RPi.GPIO.cleanup()
