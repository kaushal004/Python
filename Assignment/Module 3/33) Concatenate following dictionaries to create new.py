"""

QUE : Write a python program to concatenate following dictionaries to create a new one.



# SOLUTION : 

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)  # here create a new one dictionary.
print("dic4 : ",dic4)

"""

dic1 = {
    "Brand" : "Land Rover",
    "Model" :  "Defender"
}

dic2 = {
    "Brand" : "Mercedes",
    "Model" : "G-wagon"
}

dic3 = {}

for d in (dic1, dic2) : dic3.update(d)
print("dic3 : ",dic3)