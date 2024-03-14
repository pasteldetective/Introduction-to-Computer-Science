#Name: Jackie Yee
#Date: 21 October 2020
#Email: jackie.yee14@myhunter.cuny.edu
#This program attempts to replicate the photo in assignment 49

print("Welcome to the total with tax calculator!")
print("Please enter the price of each item you would like to purchase, one at a time. Enter a negative number when you are done.")
itemPrice = float(input("Enter the price of an item:"))
priceCul = 0
while itemPrice >= 0:
  priceCul += itemPrice
  itemPrice = float(input("Enter the price of an item:"))
print("The total with tax is $",priceCul * 1.0875)
