# This is an attempt at brute forcing the theory 3x+1 also known as Collatz Conjecture
# The conjecture states that you start with any positive integer
# If the number is odd, you apply it to the equasion 3x+1
# If the number is even, you divide it by 2
# This continues until the x equals 1

#This asks for user input
user = input("Please enter a positive integer: ") 
InputOkay = 0

##Check for positive integer
while InputOkay == 0:
    if user.isdigit():
        InputOkay = 1
        print("Input is valid")
    else :
        print("Not a positive integer.")
        user = input("Please enter a positive integer: ") 


origin = user
counter = 0
user = int(user)

while user > 1 :
    counter = counter + 1
    if user % 2 == 0:   
        user = user / 2 
        print(user)
        continue
    else :
        user = 3 * user + 1
        print(user)
        continue
else :
    print("1 has been reached")
    print("The starting number of " + str(origin) + " took " + str(counter) + " iterations")
