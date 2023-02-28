# welcome message
print("Welcome to the global energy bill calculator")
# user input
acc_number = int(input("Enter your account number: "))
month_number = int(input("Enter your month number: "))
electricity_plan = input("Enter your electricity plan: ")
electricity_used = float(input("Enter your electricity used: "))
gas_plan = input("Enter your gas plan: ")
gas_used = float(input("Enter your gas used: "))
province = input("Enter your province abbreviation(two letters): ")

# fixed charges
fixed_monthly_fee = 120.62
fixed_gas_monthly_fee = 1.32

# electricity charges
EFIR = 8.36 * 0.01 
EFIR_more_than_1000 = 9.41 * 0.01 
EFLR = 9.11 * 0.01 

# Gas charges
GFIR = 4.56 * 0.01 
GFIR_more_than_950 = 5.89 * 0.01 
GFLR= 3.93 * 0.01 

# Converting to canadian dollars
convert = 0.01

if (province == "AB" or "BC" or "MB" or "NT" or "NU" or "QC" or "SK" or "YT"):
    tax_rate = 1.05
elif (province == "ON"):
    tax_rate = 1.13
elif (province ==  "NB" or "NL" or "NS" or "PE"):
    tax_rate = 1.15

if electricity_plan == "EFIR":
    if electricity_used <= 1000:
        electricity_bill = electricity_used * EFIR
    else:
        electricity_bill = 1000 * EFIR + ((electricity_used - 1000 ) * EFIR_more_than_1000)      
elif electricity_plan == "EFLR":
    electricity_bill = electricity_used * EFLR

if gas_plan == "GFIR":
    if gas_used <= 950:
        gas_charge = gas_used * GFIR
    else:
        gas_charge = 950 * GFIR + (gas_used - 950) * GFIR_more_than_950
elif gas_plan == "GFLR":
   gas_charge = gas_used * GFLR
    
gas_bill = gas_charge + fixed_gas_monthly_fee 

total = ((electricity_bill + gas_bill + fixed_monthly_fee) * tax_rate)

print("Thank you! Your total amount due is: $", total)






















