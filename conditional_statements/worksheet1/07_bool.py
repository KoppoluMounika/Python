
power_on = input("Is power on? (True/False): ").strip().lower() == 'true'
overcurrent = input("Is overcurrent detected? (True/False): ").strip().lower() == 'true'
overvoltage = input("Is overvoltage detected? (True/False): ").strip().lower() == 'true'

if overcurrent and overvoltage:
    print("Critical Failure")
elif overcurrent:
    print("Shut Down: Overcurrent")
elif overvoltage:
    print("Shut Down: Overvoltage")
elif power_on:
    print("System Safe")
else:
    print("System Off")
