import os
import time
import signal
import logging
import RPi.GPIO as GPIO

#Tbh there is no physical Power Off button on case, that's only a power switch
#and a Power Save button, and this button only switch case on power save state
#only after 20 minutes, that the case in power save state, the GPIO event will be sent.
#(Power save state trigger even if no action taken for 15 minutes)
#Just to say that's only a safe shutdown trigger if you forgot to poweroff it
#(And you must hope that battery last at least 35min in worst case)

#This is only the Safe Shudown, the docking HDMI switch support will be added later in other script

# Constants
POWER_PIN = 26
POWEREN_PIN = 27
SHUTDOWN_COMMAND = "poweroff"
KILL_COMMAND = "batocera-es-swissknife --emukill"

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Initialize GPIO settings
def init_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(POWER_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(POWEREN_PIN, GPIO.OUT)
    GPIO.output(POWEREN_PIN, GPIO.HIGH)
    GPIO.setwarnings(False)

# PowerOff command on GPIO event
def poweroff():
    try:
        while True:
            if GPIO.input(POWER_PIN) == GPIO.LOW:
                logging.info("Shutdown signal detected.")
                os.system(KILL_COMMAND)
                time.sleep(1)
                os.system(SHUTDOWN_COMMAND)
            time.sleep(0.5)
    except Exception as e:
        logging.error(f"Error in poweroff: {e}")
    finally:
        GPIO.cleanup()

# Graceful exit handler
def signal_handler(sig, frame):
    logging.info("Terminating program...")
    GPIO.cleanup()
    exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)  # Handle Ctrl+C
    signal.signal(signal.SIGTERM, signal_handler)  # Handle termination signals

    init_gpio()
    logging.info("GPIO initialized. Monitoring power button...")
    poweroff()