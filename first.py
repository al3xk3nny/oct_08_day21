# Challenge 1
# If x is more than 10, All 5 letters are printed.
# Otherwise (x is 10 or less) only A, D and E are printed.

# Google Python If Statement

# x = 5

# print("A")

# if x > 10:
#     print("B")
#     print("C")

# print("D")
# print("E")


# Challenge 2
# If x is more than 10, print A, B, D & E
# Otherwise (x is 10 or less) print A, C, D & E

# Google Python If Else Statement

# x = 5

# print("A")

# if x > 10:
#     print("B")
# else:    
#     print("C")
    
# print("D")
# print("E")


# Class exercise
# x = 15

# if x % 3 == 0:
#     if x > 10:
#         print("A")
# else:
#     print("B")
# Result is "A"

# Revised
# x = 9

# if x % 3 == 0:
#     if x > 10:
#         print("A")
# else:
#     print("B")
# Result is blank because the if statement is true (so the else statement doesn't run), but the nested if statement is false so nothing gets printed.

# Corrected
# x = 9

# if x % 3 == 0:
#     if x > 10:
#         print("A")
#     else:
#         print("B")
# Result is "B"


# Challenge 3
# Make all staments print.
# x = 7

# if x % 3 == 0:
#     if x > 10:
#         if x == 15:
#             print("Ooooh! 15!!!")
#         else:
#             print("Boring")
#     else:
#         print("B")
# else:
#     print("C")

# print("Done")
# Answer:
# x = 15
# x = 12
# x = 9
# x = 7
# Result is: minimum of 4 values to print all statements.


# Challenge 4
# Print "B" as many time as the value of x using a while loop.
x = 5

print("A")

n = 0
while n < x:
    print("B")
    n = n + 1
    
print("C")
print("D")
print("E")
