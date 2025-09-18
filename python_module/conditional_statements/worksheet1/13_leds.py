
led1 = int(input("Enter LED1 status (0 or 1): "))
led2 = int(input("Enter LED2 status (0 or 1): "))
led3 = int(input("Enter LED3 status (0 or 1): "))

on_leds = []

if led1 == 1:
    on_leds.append("LED1 ON")
if led2 == 1:
    on_leds.append("LED2 ON")
if led3 == 1:
    on_leds.append("LED3 ON")
if on_leds:
    print(", ".join(on_leds))
else:
    print("All LEDs off")
