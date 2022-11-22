""""

-----------------KALYAN JWELLES-------------------

"""

name = input("Enter Your Name :")
gender = input("Enter your Gender :")
age = input("Enter your age :")
product = input("Enter Product name :")
weight = input("Enter Product Weight :")
price_pr_gram = input("Enter Current Price :")
total_gold_rate = int(weight) * int(price_pr_gram)
making_charge_per_gram = input("Enter Making Charges :")
total_making_charges = int(weight) * int(making_charge_per_gram)
total_amount = int(total_gold_rate) + int(total_making_charges)
discount = ""

print("----------WELCOME TO KALYAN JWELLES----------")
print("Name :", name)
print("Gender :", gender)
print("Age :", age)
print("Poduct name :", product)
print("Weight in gram :", weight)
print("Current price per Gram :", price_pr_gram)
print("TOTAL GOLD RATE :", total_gold_rate)
print("Making charges per Gram :", making_charge_per_gram)
print("Total making charges :", total_making_charges)
print("TOTAL AMOUNT :", total_amount)

#-----------MALE---------------------

if gender=="male":
    if int(age)>65:
        if total_gold_rate>=200000 and total_gold_rate < 300000:
            print("Discount 20%")
            discount = int(total_gold_rate)*20/100
            print("Discounted Total :", total_gold_rate-discount+total_making_charges)
        elif total_gold_rate>=300000 and  total_gold_rate < 500000:
            print("Discount 30%")
            discount = int(total_gold_rate)*30/100
            print("Discounted Total :", total_gold_rate-discount+total_making_charges)
        elif total_gold_rate>=500000:
            print("Discount 35%")
            discount = int(total_gold_rate)*35/100
            print("Discounted Total :", total_gold_rate-discount+total_making_charges)
        else:
            print("No Discount")
            
    else:
        
        if total_gold_rate>=200000 and total_gold_rate < 300000:
                print("Discount 10%")
                discount = int(total_gold_rate)*10/100
                print("Discounted Total :", total_gold_rate-discount+total_making_charges)
        elif total_gold_rate>=300000 and total_gold_rate < 500000:
                print("Discount 20%")
                discount = int(total_gold_rate)*20/100
                print("Discounted Total :", total_gold_rate-discount+total_making_charges)
        elif total_gold_rate>=500000:
                print("Discount 25%")
                discount = int(total_gold_rate)*25/100
                print("Discounted Total :", total_gold_rate-discount+total_making_charges)
        else:
        
            print("No Discount")

#---------FEMALE------------

if gender=="female":
    if int(age)>65:
        if total_gold_rate>=200000 and total_gold_rate<300000:
            print("Discount 25%")
            discount = int(total_gold_rate)*25/100
            print("Discounted Total :", total_gold_rate-discount+total_making_charges)
        elif total_gold_rate>=300000 and total_gold_rate<500000:
            print("Discount 35%")
            discount = int(total_gold_rate)*35/100
            print("Discounted Total :", total_gold_rate-discount+total_making_charges)
        elif total_gold_rate>=500000:
            print("Discount 40%")
            discount = int(total_gold_rate)*40/100
            print("Discounted Total :", total_gold_rate-discount+total_making_charges)
        else:
            print("No Discount")
    else:
            
        if total_gold_rate>=200000 and total_gold_rate<300000:
            print("Discount 15%")
            discount = int(total_gold_rate)*15/100
            print("Discounted Total :", total_gold_rate-discount+total_making_charges)
        elif total_gold_rate>=300000 and total_gold_rate<500000:
            print("Discount 25%")
            discount = int(total_gold_rate)*25/100
            print("Discounted Total :", total_gold_rate-discount+total_making_charges)
        elif total_gold_rate>=500000:
            print("Discount 30%")
            discount = int(total_gold_rate)*30/100
            print("Discounted Total :", total_gold_rate-discount+total_making_charges)
        else:
            print("No Discount")
            



print("--------THANK YOU FOR SHOPPING WITH US--------")
print("-----------------SEE YOU SOON-----------------")