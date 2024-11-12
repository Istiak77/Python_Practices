unit = input("Celcius or Fahrenheit?(C/F): ").upper()
temp = float(input("Enter the temperature: "))
if unit == "C":
    temp = round((9*temp)/5 + 32, 1)
    print(f"Temperature in Fahremheit is: {temp}F")
elif unit == "F":
    temp=round((temp-32)*5 / 9, 1)
    print(f"Temperature in Celcius is: {temp}C")
else:
    print(f"{unit} invalid unit.")