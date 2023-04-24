#----- practice 1
# age = int(input("enter age: "))
# expected_age = 90
# left_age = expected_age - age
# days = left_age * 365
# weeks = left_age * 52
# months = left_age * 12
# print(f" you have {days} days, you have {weeks} days, you have {months} months left")


#-----tip calculator, question- the bill is $150 split btwn 5 people with 12% tip. how much shud each person pay.
# bill = float(input(" enter bill: "))
# people = int(input(" enter number of people: "))
# tip = float(12 / 100)
# bill_with_tip = bill + (tip * bill)
# for_one_person = bill_with_tip / people
# print(f"each person pays {for_one_person} ")

#---- write a program that works out if a given number is an odd or even number.
# number = int(input("enter a number")) # if number % 2 ==0:
#   print("this is an even number")
# else:
#   print("this is an odd number")

 
# write a program that interprets the body mass index BMI based on the weight and height. <18.5 is underweight. 18.5<x<25 is normal weight.25<x<30 is obese. >35 is cinically obese.
# height = float(input("enter height"))
# weight = float(input("enter weight"))
# bmi = round(weight / height ** 2)
# if bmi < 18.5:
#     print("this is underweight")
# elif 18.5<bmi<25:
#     print("this is normal weight")
# elif 25<bmi <30:
#     print("this is obese weight")
# else:
#     print("this is clinically obese")
           
                   
# write a program that works out if a given year is a leap year.
# year = int(input("enter year"))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#            print("it is a leap year")
#         else:
#             print("it is not a leap year")
#     else:
#         print("it is not a leap year")     
# else:
#     print("it is not a leap year") 

# create an automatic pizza order program based on the user's order, calculate their bill.  

# def get_province():
#     province = input("enter province: " )
    
#     if province == True:
#         return "ab"
        
#     else:
#         province = input("enter province: ")
#         return province

# province = input("enter province: " )
# def get_tax_rate(province):

    
#     # prov ={"ab" : 1,
#     #         "bc": 2
#     #         }
    
#     if province == "ab":
#        return 1
#     elif province == "bc":
#         return 2
#     else:
#         return 3
        
# print(get_tax_rate(province))
 
 
    # OR
   
    
# prov ={"ab" : 1,
#        "bc": 2}

# def get_tax_rate():
#     province = input("enter province: " )
#     tax_rate = prov.get(province)
#     if tax_rate is None:
#         tax_rate = 3
#     return tax_rate
    
#     if province == "ab":
#         return 1
#     elif province == "bc":
#          return 2
#     else:
#         return 3
    
# prov_tax_rate =get_tax_rate()
# print(f"tax is: {prov_tax_rate}")
    
    
    
    