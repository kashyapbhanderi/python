item=input("What whould to like to buy?:")
price=float(input("What is the price?:"))
quantity=int(input("How many would you like?:"))
total=price*quantity
print(f"You have bought{quantity} x {price}/s")
print(f"Your total is:${total}")
