weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
    weight *= 2.205
    unit = "Lbs."
    print(f"Your weight is {round(weight, 2)} {unit}")
elif unit == "L":
    weight /= 2.205
    unit = "kgs"
    print(f"Your weight is {round(weight, 2)} {unit}")
else:
    print(f"{unit} is not valid.")
