# # 1. Perform addition and division
# #.....................ADDITION................................
# first_num = float(input("Enter first number: "))
# sec_num = float(input("Enter second number: "))

# addition = first_num + sec_num

# print(f" sum: {first_num} + {sec_num} = {addition}")


# #.......................DIVISION............................
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# if num2 == 0:
#     print("division error, not allowed")
# else:

#     division = num1 / num2

#     print(f" {num1} / {num2} = {division}")


# #2.........................AREA OF A TRIANGLE.............................
# base = float(input("Enter the length of the base: "))

# height = float(input("Enter the height of the triangle: "))

# Area = 0.5 * base * height

# print(f"Area of a Triangle = {Area}")


# #3........................PYTHON PROGRAMME TO SWAP TWO VARIABLES.....................
# a = input("Input value for a: ")
# b = input("Input value for b: 5")

# # Print value to display original
# print(f"original values: a = {a}, b = {b}")

# # Swap with temporary
# temp = a
# a = b
# b = temp

# print(f"swapped values are: a = {a}, b = {b}")

# #4........................GENERATE RANDOM NUMBER..................................
# import random
# print(f"Random number: {random.randint(10, 1000)}")


# #5....................Convert kilometers to miles...............................
# km = float(input("Enter value for Kilometre: "))

# # 1 kilomtre = 0.621371 miles
# conversation_rate = 0.621371

# miles = km * conversation_rate

# print(f"{km} km is equal to {miles} miles")


# #6....................Convert Celsius to Fahrenheit...........................
# celsius = float(input("Enter value for celsius: "))

# # Conversion formula: Fahrenheit = (Celsius * 9/5) + 32

# Fahrenheit = (celsius * 9/5) + 32

# print(f"{celsius} celsius is equal to {Fahrenheit} fahrenheit")


# #7........................ Python program to display calendar....................
# import calendar

# year = int(input("Enter year: "))
# month = int(input("Enter month: "))

# cal = calendar.month(year, month)

# print(cal)


# #8.............................Swap two variables without temporary..........................
# a = int(input("Enter value for a: "))
# b = int(input("Enter value for b: "))

# a, b = b, a

# print("After swapping:")
# print("a =", a)
# print("b =", b)


# #9.............................Check if a Number is Positive, Negative or Zero.............
# num = float(input("Enter number: "))

# if num > 0:
#     print("Number is positive")
# elif num == 0:
#     print("Number is zero")

# else:
#     print("Number is negative")


#10...........................CHECK IF A NUMBER IS ODD OR EVEN..............................
num = float(input("Enter number: "))

if num % 2 == 0:
    print("Number is even")

else:
    print("Number is odd")
