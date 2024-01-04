# Example Ref: https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/Ethernet%20Example%20Getting%20Started%20%5BMicropython%5D.md
# Makes the W5100s pico respond to pings from the network and blink the onboard LED while the program is running.
from machine import Pin,SPI
import network
import time

led = Pin(25, Pin.OUT)

#W5x00 chip init
def init():
    spi=SPI(0,2_000_000, mosi=Pin(19),miso=Pin(16),sck=Pin(18))
    nic = network.WIZNET5K(spi,Pin(17),Pin(20)) #spi,cs,reset pin
    nic.active(True)
    nic.ifconfig(('192.168.0.146','255.255.255.0','192.168.0.1','8.8.8.8'))

    while not nic.isconnected():
        time.sleep(1)
        print(nic.regs())

    print(nic.ifconfig())
        
def main():
    init()
    
    while True:
        led.value(1)
        time.sleep(1)
        led.value(0)
        time.sleep(1)

if __name__ == "__main__":
    main()
