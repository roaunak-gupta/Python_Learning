try:
    # Code that may raise an exception
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero!")

except ValueError:
    print("Please enter a valid number.")

finally:  # finally is always run
    print("Program execution completed.")
