"""

QUE : Write a python program to unzip a list of tuples into individual lists.

"""

# SOLUTION : 

l1 = [(1, 5, 8), (2.4, 4.10, 7), (741, 842, 91.5)]

print(list(zip(*l1)))