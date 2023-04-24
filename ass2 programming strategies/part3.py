from part1 import profits_margins

print("Welcome to Circle Phones profit calculator.")
print("You can calculate the profit of the company according to a specific day or by a week, or divide the week into weekdays and weekend.")

time_period = {
    1: 1,
    2: 7,
    3: 5,
    4: 2
}
profit_achieved = 10000

while True:
    week_option = input("Enter:\n1 - for specific day\n2 - for the week\n3 - for week business days\n4 - for weekend days\n0 - exit\n")
    
    if week_option == '0':
        break
    
    if week_option == '1':
        day = input("Enter a specific day (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday): ")
        quantity_sold = int(input("Enter the quantity: "))
        total_profit = quantity_sold * profits_margins.get(int(week_option))
        print(f"Your total profit for {day} is ${total_profit}")
        continue
        
    elif week_option in ['2', '3', '4']:
        if week_option == '2':
            days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        elif week_option == '3':
            days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        else:
            days = ["Saturday", "Sunday"]
            continue
            
        total_profit = 0
        for day in days:
            quantity_sold = int(input(f"Enter the quantity sold on {day}: "))
            profit = quantity_sold * profits_margins.get(int(week_option))
            total_profit += profit
            print(f"Profit on {day}: ${profit}")
        
        print(f"Total profit for the week: ${total_profit}")
        
        if total_profit < profit_achieved:
            print(f"More hard work needed... the last {time_period[int(week_option)]} days")
    
    else:
        print("Invalid option. Please enter a number between 0 and 4.")
