import time
from machine import Pin,reset

try:
    pin = Pin(2, Pin.OUT)
    for i in range(2):
        pin.value(0)
        time.sleep_ms(300)
        pin.value(1)
        time.sleep_ms(300)
    import node
    node.main()
except KeyboardInterrupt:
    pin.value(1)
    print("Control-C detected")

