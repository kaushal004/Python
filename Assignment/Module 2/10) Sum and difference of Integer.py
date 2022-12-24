"""

QUE : Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

"""

# SOLUTION :

num1 = int(input("Enter 1st numbar : "))
num2 = int(input("Enter 2nd number : "))

if num1+num2==5 or num1==num2 or num1-num2==5 or num2-num1==5:
    print(True)
else:
    print("False")