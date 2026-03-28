# WHILE LOOP
# while loop will execute a block of code while the condition is true
#1. --------------------------------------------------------------
value = 1

# while value <= 10:
#     print(value)
#     # if I want to stop loop at 5
#     if value == 5:
#         break    
#     value += 1

#2. -----------------------------------------------------------------

# # Continue statement
# while value <= 10:
#     value += 1
    
#     if value == 5: # 5 will not make the output because the continue statement means skip it.
#         continue
#     print(value)

# else: # this will only run when the while loop is no longer true (greater than 10).
#     print("value is now equal to " + str(value))
    
#3. --------------------------------------------------------------------
# FOR LOOP
# for loop will iterate over a sequence; contents of a collection of data types.

names = ['Dave', 'Sarah', 'Mary', 'Chidi']

# for name in names: # we can use for anything (name, x, etc.)
#     print(name)

#4. ---------------------------------------------
# for x in "Kafanchan":
#     print(x)
# # This iterates and prints every letter in Kafanchan

# #5. --------------------------------------------------------
# # Break statement, it prints everything before Mary.
# for x in names:
#     if x == "Mary":
#         break
#     print(x)

# #6. --------------------------------------------------------
# # Continue statement, it prints everything before and after Mary, skips Mary.
# for x in names:
#     if x == "Mary":
#         continue
#     print(x)

#7. ------------------------------------------------------
# Range
# for x in range(5):
#     print(x)

# for x in range(2, 4): # start at 2, end at 4 without 4
#     print(x)

#8. NESTED LOOP ---------------------------------------------------
names = ['Dave', 'Sara', 'Mary', 'Chidi']
actions = ['eats', 'sleeps', 'codes', 'teaches']

# for name in names:
#     for action in actions:
#         print(name + " " + action +".")

#9. -------------------------------------------------
# whatever is outside (actions or names) is what happens and loops through what's inside
for action in actions:
    for name in names:
        print(name + " " + action +".")


