keep_going = 'y'
while keep_going.lower() == 'y':
    wholesale_cost = float(input("Enter the item a wholesale cost: "))
    retail_price = wholesale_cost * 2.5
    print(f"retail price{retail_price:.2f}")
    keep_going = input("Do you have another item? (Enter y for yes): ")