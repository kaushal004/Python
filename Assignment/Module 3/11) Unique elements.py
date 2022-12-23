"""

QUE : Write a function that takes a list and returns a new list with unique elements of the first list.

"""

def get_uniqList(inputList):
       print('Unique List Is : ',[*set(inputList)]) 


a =  [1,2,5,1,8,5,2,6,5,9,26,22,1,1,1,1]
uniq = get_uniqList(a)
