Keep_going = 'y'

while Keep_going == 'y':
    sales = float(input("Enter the amount of sales : "))
    comm_rate = float(input("Enter the commission rate : "))
    commision = sales * comm_rate

    print(f'The commission is ${commision:.2f}')
    Keep_going = input('Do you want to  calculate another')