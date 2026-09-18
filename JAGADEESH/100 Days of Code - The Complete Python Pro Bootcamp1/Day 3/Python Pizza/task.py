print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()
price = 0
pepperoni_price = 0
cheese_price = 0

if size == "s":
    price = 15
    print("Your order is ",size)

elif size == "m":
    price = 20
    print("Your order is ", size)

elif size == "l":
    price = 30


    print("Your order is ", size)

else:
    print("incorrect size ")

if pepperoni == "y":
    if size == "s":
        pepperoni_price = 2
    elif size == "m" or size == "l":
        pepperoni_price = 3

if extra_cheese == "y":
    cheese_price = 1
    print("Your order is ", size)


print(f"your final bill  ${price + pepperoni_price + cheese_price}")