"""

QUE : Write a python program to replace last value of tuples in a list.

"""

# SOLUTION : 

list = [("black","green","yellow"), ("red","brown","grey"), ("blue","violet","orange")]
print(list)

print([x[:-1] + ("white",) for x in list])