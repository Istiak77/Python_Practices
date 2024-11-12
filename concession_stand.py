menu = {
    "pizza"   : 3.00,
    "hot dog" : 2.20,
    "lemonade": 1.00,
    "soda"    : 2.00,
    "chips"   : 1.50,
    "popcorn" : 2.00,
    "fries"   : 2.00
}

cart = []
total = 0

print("---------MENU----------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------------------")

while True:
    food = input("Select an item or (Q) to quit: ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("--------Your Orders-------")

for food in cart:
    total += menu.get(food)
    print(food)

print()
print(f"Total is: {total:.2f}")