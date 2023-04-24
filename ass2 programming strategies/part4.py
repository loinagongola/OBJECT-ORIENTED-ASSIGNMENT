from part1 import profits_margins

print("welcome to circle phones profit calculator")
print("you can calculate the profit of the company according to a specific day or by a week or divide the week into weekdays and weekend")

time_period = {
    1: 1,
    2: 7,
    3: 5,
    4: 2
}
total_profit2 = 0
profit_achieved = 10000
week =input("enter:\n1- for specific day\n2- for the week\n3- for week business days\n4- for weekend days\n0- exit\n")

while true:
    days = input("enter a specific day (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday): ")
    print(f"For {days}")
    while True:
        user_entry = int(input("enter the user entry number between 1-4, or enter 0 to stop: ")
)
        
        if user_entry == 0:
            break
        if user_entry not in range(1,5):
            print("invalid product category, please enter a number between 1 and 4.")
            continue
    
    # if week == '1':
    #     day = input("Enter a specific day (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday): ")
    #     # quantity_sold = int(input("Enter the quantity: "))
    #     # total_profit = quantity_sold * profits_margins.get(int(week))
    #     # print(f"Your total profit for {day} is ${total_profit}")
    #     # continue
    # elif week in ['2', '3', '4']:
    #     if week == '2':
    #         days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    #     elif week == '3':
    #         days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    #     else:
    #         days = ["Saturday", "Sunday"]
    #         continue

    quantity_sold = int(input("Enter the quantity: "))
    
    profit2 = quantity_sold * profits_margins.get((user_entry))
    total_profit2 += profit2
print(f"Your total profit for {days} is ${total_profit2}")
        
if total_profit2 < profit_achieved:
    print(f" we didnt reach our goal for this period.More hard work needed")
else:
    print("you did well this period! keep up the great work")

        