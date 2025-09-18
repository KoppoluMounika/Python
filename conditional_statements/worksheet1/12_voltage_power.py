# Get voltage and current input from the user
voltage = float(input())
current = float(input())

voltage_ok = 3.0 <= voltage <= 3.3
current_ok = 10 <= current <= 500
if voltage_ok and current_ok:
    print("Power OK")
elif not voltage_ok and not current_ok:
    print("Power Error")
elif not voltage_ok:
    print("Voltage Error")
elif not current_ok:
    print("Current Error")
