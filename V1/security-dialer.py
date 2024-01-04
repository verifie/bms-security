import network
import gc
import urequests
import socket
import time
from machine import Pin,SPI


# Define the GPIO pins on the Raspberry Pi Pico.
gpio_pins = [0, 1, 2, 3, 4, 5, 6, 7]

# Define the Pico LED.
led = Pin(25, Pin.OUT)

# Initialize the cycle tally
global tally
tally = 0

# Enable logging / Calling the alarm (Trigger VOIP Dialer via IFTTT)
global enable_logging
enable_logging = True
print("Logging: ", enable_logging)

global enable_calling
enable_calling = True
print("Calling: ", enable_calling)


# Initialize a dictionary to store the state of each pin
pin_states = {pin: None for pin in gpio_pins}

# -----------------------------------------------------------------------------------------
def init():
    spi=SPI(0,2_000_000, mosi=Pin(19),miso=Pin(16),sck=Pin(18))
    nic = network.WIZNET5K(spi,Pin(17),Pin(20))
    nic.active(True)
    nic.ifconfig(('192.168.0.146','255.255.255.0','192.168.0.1','8.8.8.8'))

    while not nic.isconnected():
        time.sleep(1)
        print(nic.regs())
        
    print(nic.ifconfig())


# -----------------------------------------------------------------------------------------
def callalarm():

    print("... Calling the alarm!")

    print("Call URL - 1 : Phone setup (IFTTT: volume up)")
    
    try:
        r = urequests.get("https://maker.ifttt.com/trigger/studio_alarm_security/with/key/B2OFJUMm6CTKGtzbHCE59?value1=value1&value2=value2&value3=value3")
        print(r)
        r.close()  # Close the connection
    except Exception as e:
        print(e)

    time.sleep(5)

    print("Call URL - 2 : Call IFTTT Mobile App")
    
    try:
        r = urequests.get("https://maker.ifttt.com/trigger/studio_alarm_security_call/with/key/B2OFJUMm6CTKGtzbHCE59?value1=value1&value2=value2&value3=value3")
        print(r)
        r.close()  # Close the connection
    except Exception as e:
        print(e)

    time.sleep(20)

    print("Call URL - 2 : Call IFTTT Mobile App")
    
    try:
        r = urequests.get("https://maker.ifttt.com/trigger/studio_alarm_security_call/with/key/B2OFJUMm6CTKGtzbHCE59?value1=value1&value2=value2&value3=value3")
        print(r)
        r.close()  # Close the connection
    except Exception as e:
        print(e)




# -----------------------------------------------------------------------------------------
def read_gpio_states():
        
    for pin_number in gpio_pins:

        # Draw a line if starting from pin 0
        if pin_number == 0:

            # Increment the cycle tally
            global tally

            # Reset the cycle tally if it reaches 604800 (2 weeks as the cycle is 2 seconds long)
            if tally == 604800:
                tally = 0
            tally = tally + 1

            # Print the input group divider and the cycle tally
            print("------------------------------------------------ Program Cycle: ", tally)

                # Initialize the pin in input mode
        pin = Pin(pin_number, Pin.IN)

        # Read the current state of the pin
        current_state = pin.value()
        
        # Print the state of the pin
        print(f"GPIO{pin_number+1}: {current_state}")


        # Check if the state has changed
        if pin_states[pin_number] != current_state:
            pin_states[pin_number] = current_state  # Update the state in the dictionary

            # Perform actions only if the state is 0 (and thus changed to 0)
            if current_state == 0:

                global enable_logging
                if enable_logging:

                    print("Log the trigger")

                    # Set up the states
                    states = 1

                    # Set up the trigger URL
                    trigger_url = ("https://bms.conceptstudios.co.uk/security.php?s=" + str(pin_number+1) + "&k=" + str(states))
                    print("Trigger URL: ", trigger_url)

                    try:
                        r = urequests.get(trigger_url)
                        print(r)
                        r.close()  # Close the connection
                    except Exception as e:
                        print(e)

                global enable_calling
                if enable_calling:
                    print("***********\n\nCalling Enabled.\nCall the alarm!")
                    callalarm()
                    print("Call the alarm - DONE.")

            else:
                print("Log the trigger")

                # Set up the states
                states = 0

                # Set up the trigger URL
                trigger_url = ("https://bms.conceptstudios.co.uk/security.php?s=" + str(pin_number+1) + "&k=" + str(states))
                print("Trigger URL: ", trigger_url)

                try:
                    r = urequests.get(trigger_url)
                    print(r)
                    r.close()  # Close the connection
                except Exception as e:
                    print(e)
    



# -----------------------------------------------------------------------------------------
def main():
    init()
    while True:
        
        #Set hardware LED to ON to signify a new cycle.
        led.value(1)
        
        # Read GPIO states, then act if required.
        read_gpio_states()
        
        # Wait for a second.
        time.sleep(1)
        
        # Set hardware LED to off to signify end of cycle.
        led.value(0)
        
        # Clear memory
        gc.collect()
        
        # Wait a second before next cycle
        time.sleep(1)


# -----------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()


