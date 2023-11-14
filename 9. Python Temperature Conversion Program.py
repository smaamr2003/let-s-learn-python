
temperature = float(input("Enter the temperature: "))
unit = input("Is the temperature in Celsius or Farenheit? (C/F): ")

if unit == "C":
    temperature = round(((9/5) * temperature) + 32, 1)
    print(f"The temperature in Farenheit is: {temperature}°F")
elif unit == "F":
    temperature = round((temperature - 32) * (5/9), 1)
    print(f"The temperature in Celsius is: {temperature}°C")
else:
    print(f"{unit} is not a valid unit.")