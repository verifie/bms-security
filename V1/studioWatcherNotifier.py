# securityWatcherNotifier

# Author: Paul Emerton


# ====================================================================================================
# Description: This script monitors various systems including security alarm, fire alarm, IT systems and BMS sensors and control states, and if appropriate, notifies the caretaker(s).
# Version: 1.0.0


# ====================================================================================================
# Version History
#
# 2023-12-19 - PE - Created
# 2023-12-19 - PE - Added logging
# 2023-12-19 - PE - Dummy IFTTT (If this then that) integration using Webhooks (KISS).
# 2023-12-19 - PE - Added security alarm check and notification.
# 2023-12-19 - PE - Added Raspberry Pi GPIO sensing and triggering.


# ====================================================================================================
# Dependencies: 

#   Actions:
#       IFTTT account (If this then that) - https://ifttt.com/
#       IFTTT Webhooks - https://ifttt.com/maker_webhooks
#       IFTTT Mobile App - https://ifttt.com/mobile
#       Two webhooks (one for phone setup, one for phone call). This allows the phone to change settings and then react, without a race issue causing the VOIP call to be silenced.
#   Triggers:
#       Raspberry Pi GPIO 0 volt relay triggers (Via Opto Isolators)

# ====================================================================================================
# Import libraries
#
import time
import datetime
import logging
import logging.handlers
from urllib.request import urlopen
import RPi.GPIO as GPIO           # Allows us to call our GPIO pins and names it just GPIO

# ====================================================================================================
# Import custom libraries
#


# ====================================================================================================
# Set up logging
#
logging.basicConfig(filename='studioWatcherNotifier.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


# ====================================================================================================
# Notify
#
print("\n\n\nStudio Watcher Notifier")
print("-----------------------")
print("Started at: " + str(datetime.datetime.now()))
print("-----------------------")

# ====================================================================================================
# Set up variables
#
linkSecuritySetup   = "https://maker.ifttt.com/trigger/studio_alarm_security/with/key/B2OFJUMm6CTKGtzbHCE59?value1=value1&value2=value2&value3=value3"
linkSecurityCall    = "https://maker.ifttt.com/trigger/studio_alarm_security_call/with/key/B2OFJUMm6CTKGtzbHCE59?value1=value1&value2=value2&value3=value3"
gpioTriggerSecurity = 4  # Sets the input pin.


# ====================================================================================================
# Set up GPIO
#
GPIO.setmode(GPIO.BCM)                          # Set's GPIO pins to BCM GPIO numbering
GPIO.setup(gpioTriggerSecurity, GPIO.IN)        # Set the GPIO pin to be an input


# ====================================================================================================
# Security Alarm Check
def securityAlarmCheck():
    print(str(datetime.datetime.now()) + "Security Alarm Check")

    # Test and notify if triggered.
    if (GPIO.input(gpioTriggerSecurity) == True): # Physically read the pin now
        # print(str(datetime.datetime.now()) + "Security Alarm Check : Not Triggered")
        pass

    else:
        print(str(datetime.datetime.now()) + "Security Alarm Check : Not Triggered")
        securityAlarmNotify() # Trigger notifications to site caretaker(s).


# ====================================================================================================
# Notification Functions
#
def securityAlarmNotify():
    
    # Fire URL 1 : Phone setup (IFTTT: volume up)
    print(str(datetime.datetime.now()) + "Fire URL 1 : Phone setup (IFTTT: volume up)")
    with urlopen(linkSecurityCall) as response:
        urlOutputRead = response.read()
    print(urlOutputRead)

    # WAIT 5 SECONDS to allow phone to react.
    time.sleep(5)

    # Fire URL 2 : Call IFTTT Mobile App
    print(str(datetime.datetime.now()) + "Fire URL 2 : Call IFTTT Mobile App")
    with urlopen(linkSecurityCall) as response:
        urlOutputRead = response.read()
    print(urlOutputRead)


    # Now repeat the call requests to mitigate race conditions (phone not reacting in time or phone signal issues).

    # WAIT 5 SECONDS to allow phone to react.
    time.sleep(5)

    # Fire URL 2 : Call IFTTT Mobile App
    print(str(datetime.datetime.now()) + "Fire URL 2 : Call IFTTT Mobile App")
    with urlopen(linkSecurityCall) as response:
        urlOutputRead = response.read()
    print(urlOutputRead)

    # WAIT 5 SECONDS to allow phone to react.
    time.sleep(10)

    # Fire URL 2 : Call IFTTT Mobile App
    print(str(datetime.datetime.now()) + "Fire URL 2 : Call IFTTT Mobile App")
    with urlopen(linkSecurityCall) as response:
        urlOutputRead = response.read()
    print(urlOutputRead)