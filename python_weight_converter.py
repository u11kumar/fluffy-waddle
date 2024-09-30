# Python Weight Converter

weight=float(input("Enter your weight: "))
unit=input("you want your weight in Kilograms or Pounds? (K or L):")
unit=unit.upper()
if unit == "K":
    converted_weight = weight * 2.205
elif unit == "L":
    converted_weight = weight/2.205
else:
    print(f"{unit} was not valid")

print(f"Your weight is {round(converted_weight,1)} {unit}")