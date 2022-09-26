#this creates a list of years from 0 to 4000
years = list(range(4001))

#this loops from 0 to 4000
for x in years :
    #this looks to see if the number being checked is divisable by 4
    if x % 4 == 0 :
        #check to see if it is also divisible by 100
        if x % 100 != 0 :
            #if it is divisible by 4 but not 100, remove it from the list
            years.remove(x)
    #if it is divisible by 400, remove it from the list        
    if x % 400 == 0 :
            years.remove(x)

print(years)