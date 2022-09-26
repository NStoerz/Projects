#I was given this prompt/challenge from a friend:

#Create a list of 30 random integers from 1 to 9
#Count how many items in your random list are odd
#Return the random list and the count of odds
#Additional challenge is to rewrite this so that it only uses 1 loop
#Bonus challenge: ask the user for input. Have it prompt for how long the list should be and the max value for the random numbers

length = input ("Enter the length of the string :")
max = input ("Enter the maximum number :")

import random
randomlist = []
OddNumber=0 
for i in range (0,int(length)):
    n = random.randint(0,int(max))
    randomlist.append(n)
    if n % 2 != 0:
        OddNumber = OddNumber + 1
print("There are " + str(OddNumber) + " odd numbers")
print(randomlist)
