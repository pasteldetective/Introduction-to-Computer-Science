#Name: Jackie Yee
#Date: 21 October 2020
#Email: jackie.yee14@myhunter.cuny.edu
#This program attempts to replicate the photo in assignment 40

def main():
    
    inQ1 = int(input("What year are you? (1,2,3,4):"))
    inQ2 = int(input("How old are you?:"))
    inQ3 = str(input("Are you currently on probation? (Yes or No):"))
    inQ4 = int(input("Are you Part-time or Full-time? (0 or 1):"))
    inQ5 = float(input("What is your GPA?"))
    answers = [inQ1, inQ2, inQ3, inQ4, inQ5]
    housingScore = computeScore(answers)
    print(housingScore)


def computeScore(answers):
    houseScore = 0
    if (answers[0] == 1):
        houseScore += 1
    elif (answers[0] == 2):
        houseScore += 2
    elif (answers[0] == 3):
        houseScore += 3
    elif (answers[0] == 4):
        houseScore += 4

    if (answers[1] >= 23):
        houseScore += 1

    if (answers[2] == "Yes"):
        houseScore -= 1

    if (answers[3] == 1):
        houseScore += 1

    if (answers[4] >= 3.5):
        houseScore += 1

    return houseScore
    

#Allow script to be run directly:
if __name__ == "__main__":
     main()
