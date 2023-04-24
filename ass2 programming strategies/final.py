# Continuation of part 1.
# This programme allows the user to select time period and outputs total profit.
# Constants, lists, dictionaries. Each function will be used in the code.
days_of_the_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
time_periods = {"1": days_of_the_week, 2: "this Week", 3: "these Business days", 4: "this Weekend"}
product_prices = {"1": 120.45, "2": 99.50, "3": 75.69, "4": 65.73, "5": 51.49}
achieved_profit = 10000
loop_back = True
# Section is not included in loop as per test output.
print("Welcome to Circle Phones’ Profit calculator."
      " You can calculate your profits for a specific day, "
      "by week or you can divide the week into weekdays and the weekend")
print("Welcome to Circle Phones Profit calculator \n")

# Loop begins depending on users inputs. total_price, total_profit are constants defined in the loop.
while loop_back:
    total_price = 0
    total_profit = 0
    user_selected_day = ""
    print("You can calculate the profit of the company according to a specific day or by a week or divide"
          " the week into weekdays and weekend")
    print("Enter: \n 1 - For specific day \n 2 - For the week \n 3 - For week business days \n 4 - For weekends \n "
          "0 - Exit")

    user_time_period = int(input())
    if user_time_period in [1, 2, 3, 4]:
        if user_time_period == 1:
            while True:
                # Incorrect input results in loop
                print("Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday].")
                user_selected_day = str(input()).strip().lower()
                if user_selected_day not in days_of_the_week:
                    continue

                break
            time = [user_selected_day]
        elif user_time_period == 2:
            time = days_of_the_week
        elif user_time_period == 3:
            time = days_of_the_week[0:5]
        else:
            time = days_of_the_week[5:7]

        for day in time:
            print(f"for {day}")
            while True:
                user_product_number = str(input("Enter product number 1-5, or enter 0 to stop:\n "))
                if user_product_number in product_prices:
                    user_quantity = int(input("Enter quantity sold:\n "))
                    total_price += user_quantity * product_prices.get(user_product_number)
                elif user_product_number == "0":
                    break
                else:
                    print("you have not specified between the numbers 1-5. Please specify.")

    elif user_time_period == 0:
        loop_back = False
        print("Programme end!")
        break
    # Invalid input restarts loop.
    else:
        print("Invalid input, please enter valid input")
    # Result prints based total price attained.
    if total_price != 0:
        print(f"Your profit for {time_periods.get(user_time_period, user_selected_day)} is: ${round(total_price, 2)}")
        if total_profit < achieved_profit:
            print(f"More hard work needed... "
                  f"The last {time_periods.get(user_time_period, user_selected_day)} wasn't the best")
        else:
            print(f"You did well {time_periods.get(user_time_period, user_selected_day)}! Keep up the great work!")
