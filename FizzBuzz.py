# Fizz buzz is a group word game for children to teach them about division.
# Players take turns to count incrementally.
# Replace any number divisible by three with the word "fizz", 
# Any number divisible by five with the word "buzz".
# Numbers divisible by 15 become fizz buzz.

fizz = 0
buzz = 0
fizzbuzz = 0

for num in range (50) :
    if num % 3 == 0 and num % 5 == 0 :
        fizzbuzz = fizzbuzz + 1
        print ("fizzbuzz")
        continue
    elif num % 3 == 0 :
        fizz = fizz + 1
        print("fizz")
        continue
    elif num % 5 == 0 :
        buzz = buzz + 1
        print("buzz")
        continue
    print(num)
print("There are " + str(fizz) + " fizzes." )
print("There are " + str(buzz) + " buzzes." )
print("There are " + str(fizzbuzz) + " fizzbuzzes." )
    
        