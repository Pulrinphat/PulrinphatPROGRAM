Select = input("Select opeations form 1,2,3,4 :")
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
if Select == "1":
    sum =number1 + number2
elif Select == "2" :
    sum = number1 - number2
elif Select == "3":
    sum = number1 * number2
elif Select == "4":
    sum = number1 / number2
print(sum)
