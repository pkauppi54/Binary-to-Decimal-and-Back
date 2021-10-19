import math
n = int(input("Input a number"))
binary = []
quotient = n
while quotient//2 != 0:
    
    remainder = quotient%2
    binary.append(remainder)
    quotient = quotient//2
        
    print(f"Quotient {quotient}")
    
    continue

binary.append(1)

binary.reverse()
print(binary)






    
    
