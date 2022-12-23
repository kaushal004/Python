"""

QUE : Write a python program to remove an empty tuple(s) from a list of tuples.

"""

# SOLUTION : 

list = [("Kaushal ","Good","Best"), ("Github"), (2.1,6,0), (), (''), ("J")]
list = [t for t in list if t]
print(list)
