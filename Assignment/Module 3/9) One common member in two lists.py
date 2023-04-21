"""

QUE : Write a python function that takes two lists and return true if they have at least one common member.

"""

# SOLUTION :

def common(a, b):
    result = [i for i in a if i in b]
    return result

a = [1,2,3]
b = [3,5,4]

print(common(a, b))