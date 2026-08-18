from machine import Pin
import time

led_red = Pin(15, 1)
led_yellow = Pin(11, 1)
led_green = Pin(14, 1)

led_red.value(0)
led_yellow.value(0)
led_green.value(1)

while True:
    time.sleep(5)
    
    led_red.value(0)
    led_yellow.value(1)
    led_green.value(0)

    time.sleep(2)

    led_red.value(1)
    led_yellow.value(0)
    led_green.value(0)

    time.sleep(5)

    led_red.value(1)
    led_yellow.value(1)
    led_green.value(0)

    time.sleep(2)

    led_red.value(0)
    led_yellow.value(0)
    led_green.value(1)

    time.sleep(5)