
import random
#Generates a random number
danum = random.randrange(0, 1024)

#starts the loop until you hit the number
while(True):
    #Gets a number from the user
    usersnum = input("Type in a number: ")
    #Casts to an interger
    usersnum = int(usersnum)
    #checks if the number is less than number given if so tells user that they are high
    if danum < usersnum:
        print("You are High")
    # checks if the number is higher than number given if so tells user that they are high
    elif danum > usersnum:
        print("You are low")
    # Kill switch if the number is chosen and exits the loop
    else:
        print("You hit the number")
        break
#Congragulation message to the user.
print("Congrats on finding the number")
