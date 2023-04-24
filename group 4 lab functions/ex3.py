def average(n):
    numbers = 0
    if n > 1:
        for i in range(1, n + 1):
            numbers = numbers + i
        avg = numbers / n
        print(f"The average of integers from 1 to {n} is {avg}")

average(5)
