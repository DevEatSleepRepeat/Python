import machine
import utime

ObLED = machine.Pin(25, machine.Pin.OUT)

while True:
    ObLED.value(1)
    utime.sleep(2)
    ObLED.value(0)
    utime.sleep(2)