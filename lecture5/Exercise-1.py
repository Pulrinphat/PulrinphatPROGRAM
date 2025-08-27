def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == num
print(is_armstrong(153))   
print(is_armstrong(9474))  
print(is_armstrong(123))     