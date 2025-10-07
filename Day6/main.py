# Exception handling 
#  Exception is an event that occurs during the execution of a program that disrupts the normal flow of instructions.

#  Example 1: ZeroDivisionError
a = int(input("Enter a number: "))

result = 10/a
print("The result is:", result)

print("ok i have done the division")

# Example 2: ValueError

b = int(input("Enter another number: "))
print("The number you entered is:", b)
print("ok i have printed the number")
print("ok i have done the printing")

# Example 3: IndexError
# my_list = [1, 2, 3, 4, 5]
# print(my_list[10])
# print("ok i have printed the list")
# print("ok i have done the printing")

# Keywords in Exception

# try: The code that may raise an exception is placed inside the try block.
c = int(input("Enter a number: "))
try:
    result = 10/c
    print("The result is:", result)
except Exception as e:
    print("Error: Division by zero is not allowed.{e}")

print("ok i have done the division")     


# Else: The code inside the else block is executed if no exceptions are raised in the try block.

try:
    result = 10/c
    print("The result is:", result)
except Exception as e:
    print("Error: Division by zero is not allowed.{e}")

else:
    print("No exceptions occurred.")


# Finally: The code inside the finally block is always executed, regardless of whether an exception occurred or not. 

try:
    result = 10/c
    print("The result is:", result)
except Exception as e:
    print("Error: Division by zero is not allowed.{e}")

else:
    print("No exceptions occurred.")

finally:
    print("I will run no matter what.")  



# Raise: The raise keyword is used to manually raise an exception.


age = int(input("Enter your age: "))
try:
   if age < 10 or age > 18:
    raise ValueError("Age must be between 10 and 18.")
   else:
    print("Your age is valid.")
except Exception as e:
    print("Error: {e}")

print("The Club welcomes you.")

#  Handling Means to manage the exceptions that may occur during the execution of a program.

