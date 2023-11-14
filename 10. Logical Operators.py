temperature = 25
#temperature = -10
#temperature = 40

if temperature > 0 and temperature < 30:
    print("The temperature is good.")
else:
    print("The temperature is bad.")

if temperature <= 0 or temperature >= 30:
    print("The temperature is bad.")
else:
    print("The temperature is good.")

sunny = True
# Change this to either True or False

if not sunny:
    print("It is cloudy outside")
else:
    print("It is sunny outside")