"""

QUE : Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.

"""

# SOLUTION :

for i in range(1,6):
    num1 = int(input("Enter  number :"))
    if num1%2 == 0:
        print("EVEN")
    else:
        print("Odd")