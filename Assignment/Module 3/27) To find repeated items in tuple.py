"""

QUE : Write a python program to find the repeated items of a tuple.

"""

# SOLUTION : 

tup = (1,3,4,32,1,1,1)  
for i in tup:
    if tup.count(i) > 1:
        print('REPEATED')