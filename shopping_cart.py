foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy and Q to quit: ").upper()
    if food == "Q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: "))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART-----")

for food in foods:
    print(food)

for price in prices:
    total += price

print(f"Your Total is : {total}")    