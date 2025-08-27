print("Program output")
hour = int(input("Enter the number of hours worked:"))
pay = float(input("Enter the hourly pay rate:"))

if hour > 40:
    sum  = (40 * pay) + ((hour - 40) * pay * 1.5) 
else:
    sum = hour * pay 
print("The gross pay is $",float(sum))