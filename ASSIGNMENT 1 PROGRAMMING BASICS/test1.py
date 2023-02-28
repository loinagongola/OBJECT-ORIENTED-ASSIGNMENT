welcome = ("Welcome to the Global Energy bill calculator")
print(welcome)


account_number = int(input("Enter your account number: "))

month_number = int(input("Enter your month number(e.g for January, enter 1): "))

electricity_plan = input("Enter your electricity plan (EFIR or EFLR): ")

electricity_used=float(input("Enter your electricity used in month 2: "))

gas_plan = input("Enter your gas plan (GFIR or GFLR): ")

gas_used=float(input("Enter your gas used in month 2: "))

province = input("Enter the abbreviation of your province (two letters): ")

amount_due = ("Thankyou! Your total amount due is: ")

EFIR = (8.36 * 0.01)
EFIR_after_1000kWh = (9.41 * 0.01)

EFLR = (9.11 * 0.01)


GFIR = (4.56 * 0.01)

GRIR_after_950_GJ = (5.89 * 0.01)


GFLR = (3.93 * 0.01)

natural_gas_fixed_monthly_fee = (1.32 * 0.01)
fixed_monthly_fee = (120.62 * 0.01)



five_percent_tax = (1.05 * 0.01)
thirteen_percent_tax = (1.13 * 0.01)

fifteen_percent_tax = (1.15 * 0.01)


if (electricity_used >= 1000):
   electricity_cost = (( EFIR_after_1000kWh * electricity_used) + fixed_monthly_fee)
    
    if (province == "AB" or 
        province == "BC" or 
        province == "MB"or 
        province == "NT" or 
        province == "NU" or 
        province == "QC" or 
        province == "SK" or 
        province == "YT"): 
        print(electricity_cost * five_percent_tax) 

    elif (province=="ON"):
        print(electricity_cost * thirteen_percent_tax)
    
    elif (province=="NB" or 
          province == "NL" or 
          province == "NS" or 
          province == "PE" ):
          print(electricity_cost * fifteen_percent_tax)

elif (electricity_used < 1000):
    cost = (EFIR * electricity_used)
    if (province == "AB" or 
        province == "BC" or 
        province == "NT" or 
        province == "NU" or
        province == "QC" or
        province == "SK" or
        province == "YT"): 
        print(electricity_cost * five_percent_tax)
        
    elif (province=="ON"):
         print(electricity_cost* thirteen_percent_tax)
        
    elif (province=="NB" or 
          province == "NL" or 
          province == "NS" or  
          province == "PE" ):
          print(electricity_cost* fifteen_percent_tax)

if (gas_used >= 950):
    cost = (GRIR_after_950_GJ * gas_used)
    if (province == "AB" or 
        province == "BC" or 
        province == "NT" or 
        province == "NU" or
        province == "QC" or
        province == "SK" or
        province == "YT"):
        print(cost * five_percent_tax)
        
    elif (province=="ON"):
        print(cost * thirteen_percent_tax)
        
    elif (province=="NB" or 
          province == "NL" or 
          province == "NS" or 
          province == "PE" ):
          print(cost * fifteen_percent_tax)
        
elif (gas_used < 950):
    cost = (GFIR * gas_used)
    if (province == "AB" or 
        province == "BC" or 
        province == "NT" or 
        province == "NU" or
        province == "QC" or
        province == "SK" or
        province == "YT"):
        print(cost * five_percent_tax) 
    
    elif (province=="ON"):
         print(cost * thirteen_percent_tax)
    
    elif (province=="NB" or 
          province == "NL" or 
          province == "NS" or 
          province == "PE" ):
          print(cost * fifteen_percent_tax)
        
        
            
            
            
            




















