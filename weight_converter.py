weight = float(input("Enter your weight: "))
unit = input("Kilograms or Grams? (K or G): ").upper()

if unit == "K":
    weight = weight*1000
    unit = "grams."
    print(f"Your weight is: {round(weight, 1)} {unit}")
elif unit == "G":
    weight = weight/1000
    unit = "Kgs."
    print(f"Your weight is: {round(weight, 1)} {unit}")
else:
    print(f"{unit} was not a valid unit") 
