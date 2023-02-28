# Average of integers

N = int(input(" Enter a value of any integer greater than 1: "))

if N > 1:
    average = 0
    for i in range(1, N + 1):
        
        # average += i/N is the same as -------- average = (average + i) / N
        average += i / N
        
print(f"the average is equal to: {average}")
        


    
    
