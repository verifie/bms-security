import network
import urequests
import socket
import time
from machine import Pin,SPI

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
def sendData():

    print("Call URL - 1 : Phone setup (IFTTT: volume up)")
    
    try:
        r = urequests.get("https://maker.ifttt.com/trigger/studio_alarm_security/with/key/B2OFJUMm6CTKGtzbHCE59?value1=value1&value2=value2&value3=value3")
        print(r)
    except Exception as e:
        print(e)

    time.sleep(5)

    print("Call URL - 2 : Call IFTTT Mobile App")
    
    try:
        r = urequests.get("https://maker.ifttt.com/trigger/studio_alarm_security_call/with/key/B2OFJUMm6CTKGtzbHCE59?value1=value1&value2=value2&value3=value3")
        print(r)
    except Exception as e:
        print(e)

# -----------------------------------------------------------------------------------------
def main():
    init()
    sendData()


# -----------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
