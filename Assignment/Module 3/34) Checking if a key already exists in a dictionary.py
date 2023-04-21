"""

QUE : Write a python script to check if a given key already exists in a dictionary.

"""

# SOLUTION : 

d = {"Gujarat" : "Ahmedabad", "Maharastra" : "Mumbai", "Rajasthan" : "Udaipur", "Uttarpradesh" : "Lucknow"}
def key_exist(x):
    if x in d:
        print("Key exist in dictionary")
    else:
        print("Key does not exist in dictionary")

key_exist("Goa")