# Joshua Elesterio
# Matchmaker Lite 

#Constants
#INTRODUCTION

INTRODUCTION = '''

Matchmaker: Find out if you are compatible with me!

Welcome! Type an answer from 1-5 
1 means that you strongly disagree with the question
5 means that you strongly agree with the question
In the end, your score out of 100 (with 100 being a perfect compatibility)
will tell you how compatible you are with me. Give it a try!

'''
question = [
'Nirvana is the best band in the world!',
'The Philippines is the best place to live!',
'The 90s is the best time period to travel back to!',
'Tennis is the best sport in the world!',
'Thanksgiving is my favorite holiday!'
]

#INTRODUCTION
print (INTRODUCTION)

#dResponse

dResponse = [
    5,
    5,
    4,
    1,
    4
    
]


#introduction
print(INTRODUCTION)


#5 questions
userResponse1 = int(input(question[0]))
if userResponse1 <1 or userResponse1 >5:
    print("Type a number from 1-5!")
    userResponse1 = int(input(question[0]))
else:
    comp1 = 5 - abs(userResponse1 - dResponse[0])
    print("Question 1 compatability: " + str(comp1) + " out of 5!")

userResponse2 = int(input(question[1]))
if userResponse2 <1 or userResponse2 >5:
    print("Type a number from 1-5!")
    userResponse2 = int(input(question[1]))
else:
    comp2 = 5 - abs(userResponse2 - dResponse[1])
    print("Question 2 compatability: " + str(comp2) + " out of 5!")

userResponse3 = int(input(question[2]))
if userResponse3 <1 or userResponse3 >5:
    print("Type a number from 1-5!")
    userResponse3 = int(input(question[2]))
else:
    comp3 =5 - abs(userResponse3 - dResponse[2])
    print("Question 3 compatability: " + str(comp3) + " out of 5!")

userResponse4 = int(input(question[3]))
if userResponse4 <1 or userResponse4 >5:
    print("Type a number from 1-5!")
    userResponse4 = int(input(question[3]))
else:    
    comp4 =5 - abs(userResponse4 - dResponse[3])
    print("Question 4 compatability: " + str(comp4) + " out of 5!")

userResponse5 = int(input(question[4]))
if userResponse5 <1 or userResponse5 >5:
    print("Type a number from 1-5!")
    userResponse5 = int(input(question[4]))
else:
    comp5 =5 - abs(userResponse5 - dResponse[4])
    print("Question 5 compatability: " + str(comp5) + " out of 5!")

#totals and other constants
totalComp = (comp1 + comp2 + comp3 + comp4 + comp5) * 4
print("Total Compatibility out of 100! = ""You are " + str(totalComp)+ "% " + "compatible with me")