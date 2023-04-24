from part1 import profits_margins

print("welcome to circle phones profit calculator")
print("you can calculate the profit of the company according to a specific day or by a week or divide the week into weekdays and weekend")

# week =input("enter:\n1- for specific day\n2- for the week\n3- for week business days\n4- for weekend days\n0- exit\n")

time_period = {
    1: 1,
    2: 7,
    3: 5,
    4: 2
}
total_profit2 = 0
profit_achieved = 10000

while True:
    week =input("enter:\n1- for specific day\n2- for the week\n3- for week business days\n4- for weekend days\n0- exit\n")
    user_entry = int(input("enter the user entry number between 1-4, or enter 0 to stop: "))
    
    if user_entry == 0:
     break
    
    # if user_entry in range(1,5):
    #     days = input("enter a specific day (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday): ")
    #     print(f"For {days}")
        
    if user_entry == 1:
        days = input("Enter a specific day (Monday, Tuesday,Wednesday, Thursday, Friday, Saturday, Sunday): ")
        print(f"for {days}")
        # quantity_sold = int(input("Enter the quantity: "))
        continue
        
    elif user_entry in [2, 3, 4]:
        if user_entry == 2:
           days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
           print(f"for {days}")
        elif user_entry == 3:
            days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
            print(f"for {days}")
        else:
            days = ["Saturday", "Sunday"]
            print(f"for {days}")
            continue
                
    quantity_sold = int(input("Enter the quantity: "))
    profit2 = quantity_sold * profits_margins.get((user_entry))
    total_profit2 += profit2
    print(f"Your total profit for {days} is ${total_profit2}")
    
    if total_profit2 < profit_achieved:
            print(f" we didnt reach our goal for this period.More hard work needed")
    else:
        print("you did well this period! keep up the great work")

                           
    
            # quantity_sold = int(input(f"Enter the quantity sold on {day}: "))
            # profit = quantity_sold * profits_margins.get(int(user_entry))
            # total_profit += profit
            # print(f"Profit on {day}: ${profit}")
        
    # print(f"Total profit for the week: ${total_profit2}")
        
    
        
    #     quantity_sold = int(input("enter the quantity: "))
    #     # profit_2 = time_period[user_entry] * quantity_sold
    #     # total_time += profit_2
    #     # total = total_time * total_profit
    #     total_profit2 += quantity_sold *  profits_margins.get(user_entry)
    #     continue
    # else:
    #     print("invalid user entry, please enter a number between 1 and 4.")
    #     continue
    # print(f"your total profit for {days} is ${total_profit2}")
    
    # if total_profit2 < profit_achieved:
    #         print(f" we didnt reach our goal for this period.More hard work needed")
    # else:
    #     print("you did well this period! keep up the great work")

                
     
     
    

