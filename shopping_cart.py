# Shopping Cart Program

foods=[]
prices=[]
quantities=[]
total=0

while True:
    food=input("Enter a food to buy (q for quit):")
    if food.lower()=="q":
        break
    else:
        price=float(input(f"Enter the price of (each unit) {food}:₹"))
        food_quantity=int(input(f"Enter the quantity of {food}: "))
        foods.append(food)
        prices.append(price)
        quantities.append(food_quantity)
        total += price * food_quantity
        
print("\nShopping Cart Summary:")
print(f"{'Food':<20} {'Price':<10} {'Quantity':<10} {'Total':<10}")
for i in range(len(foods)):
    item_total = prices[i] * quantities[i]
    print(f"{foods[i]:<20} ₹{prices[i]:<9} {quantities[i]:<10} ₹{item_total:<10}")

print(f"\nTotal Amount: ₹{total:.2f}")