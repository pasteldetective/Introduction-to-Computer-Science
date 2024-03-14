#Name: Jackie Yee
#Date: 21 October 2020
#Email: jackie.yee14@myhunter.cuny.edu
#This program attempts to replicate the photo in assignment 47

def monthString(monthNum):
    monthString = ""

    if (monthNum == 1):
        monthString = "January"
    elif (monthNum == 2):
        monthString = "February"
    elif (monthNum == 3):
        monthString = "March"
    elif (monthNum == 4):
        monthString = "April"
    elif (monthNum == 5):
        monthString = "May"
    elif (monthNum == 6):
        monthString = "June"
    elif (monthNum == 7):
        monthString = "July"
    elif (monthNum == 8):
        monthString = "August"
    elif (monthNum == 9):
        monthString = "September"
    elif (monthNum == 10):
        monthString = "October"
    elif (monthNum == 11):
        monthString = "November"
    else:
        monthString = "December"
        


    return(monthString)



def main():
     n = int(input('Enter the number of the month: '))
     while n > 12 or n < 1:
         n = int(input('That is not a valid month numnber. Please enter the number of the month: '))
     mString = monthString(n)
     print('The month is', mString)



#Allow script to be run directly:
if __name__ == "__main__":
     main()
