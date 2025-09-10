try:
    numerator = float(input("Enter the nuerator: "))
    denominator = float(input("Enter the denominator: "))

    result = numerator / denominator
    print(f"The result is: {result}")

except ZeroDivisionError:
    print("error: You cannot divide by zero.")

except ValueError:
    print("Error: Invalid input. Please enter nameric values. ")

finally:
    print("Execution completed, whether an exception occurred or not. ")

print("End of program")