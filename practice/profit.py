profits_margins= [{
    1: 120,
    2: 99,
    3: 75,
    4: 65,
    5: 51
}]
total_profit =0

while True:
    category = int(input("enter the category number 1-5: "))
    
    if category == 0:
        break
    
    if category not in range (1,6):
        print("invalid category number, please enter the correct category number")
        continue
    
    quantity = int(input("enter the quantity number: "))
    
    profit = profits_margins[category] * quantity
    total_profit += profit
    
print(f"your total profit is ${total_profit}")
        
    