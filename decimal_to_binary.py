import math
n = input("Input a binary number: ")
decimal = 0
power = len(n)-1
for num in n:
    
    b = int(num)*2**power
    power -= 1
    decimal += b

print(decimal)
