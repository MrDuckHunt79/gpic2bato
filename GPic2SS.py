import os
import RPi.GPIO as GPIO
from multiprocessing import Process

#Tbh there is no physical Power Off button on case, that's only a power switch
#and a Power Save button, and this button only switch case on power save state
#only after 20 minutes, that the case in power save state, the GPIO event will be sent.
#(Power save state trigger even if no action taken for 15 minutes)
#Just to say that's only a safe shutdown trigger if you forgot to poweroff it
#(And you must hope that battery last at least 35min in worst case)

#This is only the Safe Shudown, the docking HDMI switch support will be added later in other script

# initialize pins
powerPin = 26
powerenPin = 27

# initialize GPIO settings
def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(powerPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(powerenPin, GPIO.OUT)
    GPIO.output(powerenPin, GPIO.HIGH)
    GPIO.setwarnings(False)


# PowerOff command on GPIO event
def poweroff():
    while True:
        GPIO.wait_for_edge(powerPin, GPIO.FALLING)
        os.system("shutdown -h now")


if __name__ == "__main__":
    # initialize GPIO settings
    init()
    # create a multiprocessing.Process instance for each function to enable parallelism
    powerProcess = Process(target=poweroff)
    powerProcess.start()

    powerProcess.join()

    GPIO.cleanup()
