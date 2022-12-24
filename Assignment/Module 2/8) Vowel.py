"""

QUE : Write a Python program to test whether a passed letter is a vowel or not.

"""

# SOLUTION :

letter = input("Enter letter : ")

if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' :
    print(letter,"is vowel")
else:
    print(letter,"is consonant")