profits_margins = {
1: 120.45,
2: 99.50,
3: 75.69,
4: 65.73,
5: 51.49
}
 
total_profit = 0

while True:
    category = int(input("enter the product category 1-5, or enter 0 to stop: "))

    if category == 0:
       break

    if category not in range(1,6):
       print("invalid product category, please enter a number between 1 and 5.")
       continue
    
    quantity_sold = int(input("enter the quantity: "))
    
    profit = profits_margins[category] * quantity_sold
    total_profit += profit

print(f"your total profit is ${total_profit}")


 