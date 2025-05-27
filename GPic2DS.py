import RPi.GPIO as GPIO
import os
import time
import logging
import signal

# Constants
HDMI_PIN = 18
CONFIG_FILE = "/boot/config.txt"
LCD_CONFIG_FILE = "/boot/lcdconfig.txt"
DS_CONFIG_FILE = "/boot/dsconfig.txt"

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Initialize GPIO settings
def init_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(HDMI_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Find lines matching a specific text in a file
def file_matching_lines(filename, txt):
    try:
        with open(filename) as f:
            return [line for line in f if txt in line]
    except FileNotFoundError:
        logging.error(f"File not found: {filename}")
        return []

# Handle HDMI or LCD configuration
def handle_display_config():
    hdmi_test = GPIO.input(HDMI_PIN)
    logging.info(f"HDMI pin state: {hdmi_test}")

    if hdmi_test == GPIO.HIGH:
        logging.info("Detected HDMI mode")
        if file_matching_lines(CONFIG_FILE, "enable_dpi_lcd=1"):
            switch_to_hdmi()
    else:
        logging.info("Detected LCD mode")
        if not file_matching_lines(CONFIG_FILE, "enable_dpi_lcd=1"):
            switch_to_lcd()

# Switch to HDMI configuration
def switch_to_hdmi():
    logging.info("Switching to HDMI configuration")
    try:
        os.system("mount -o remount, rw /boot")
        os.system("mv -f /boot/config.txt /boot/lcdconfig.txt")
        os.system("mv -f /boot/dsconfig.txt /boot/config.txt")
        os.system("batocera-audio set alsa_output._sys_devices_platform_soc_fef00700.hdmi_sound_card0.hdmi-stereo")
        os.system("shutdown -r now")
    except Exception as e:
        logging.error(f"Error switching to HDMI: {e}")

# Switch to LCD configuration
def switch_to_lcd():
    logging.info("Switching to LCD configuration")
    try:
        os.system("mount -o remount, rw /boot")
        os.system("mv -f /boot/config.txt /boot/dsconfig.txt")
        os.system("mv -f /boot/lcdconfig.txt /boot/config.txt")
        os.system("batocera-audio set alsa_output.usb-GeneralPlus_USB_Audio_Device-00.analog-stereo")
        os.system("shutdown -r now")
    except Exception as e:
        logging.error(f"Error switching to LCD: {e}")

# Monitor HDMI pin state
def monitor_display():
    while True:
        handle_display_config()
        time.sleep(1)

# Graceful exit handler
def signal_handler(sig, frame):
    logging.info("Terminating program...")
    GPIO.cleanup()
    exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)  # Handle Ctrl+C
    signal.signal(signal.SIGTERM, signal_handler)  # Handle termination signals

    init_gpio()
    logging.info("GPIO initialized. Monitoring display configuration...")
    monitor_display()