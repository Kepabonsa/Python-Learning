# Python weight converter

weight = float(input("Enter yout weight: "))
unit = input("Kilograms or Pounds?(Kl or Lb): ")

if unit == "Kl":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"Your weight is: {round(weight, 1)} {unit}")
elif unit == "Lb":
    weight = weight / 2.205
    unit = "Kgs"
    print(f"Your weight is: {round(weight, 1)} {unit}")
else: 
    print(f"{unit} was not valid")

