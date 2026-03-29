# Function are reusable blocks of code,
# when we call the function, it executes the block of code.

# def hello():
#     print("Hello World!")

# hello()

# # 2. -------------------------------------------------
# def sum(num1, num2):
#     print(num1 + num2)

# sum(2, 3)


# # 3. ---------------------------------------------------
# def sum(num1=0, num2=0):
#     return num1 + num2

# total = sum(3, 9)

# print(total)

# 4. ------------------------------------------------------
# When we have unknown number of parameters to pass, we use 'args'

def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("Dave", "Sara", "Mary", "Chidi")

# 5. kwargs
