from random import randint
# random is built-in python module for generating random integer in python

# List of input options
t = ["Stone","Paper","Scissors"]

#Assigning a random thing to PC

pc = t[randint(0,2)]

player = False

while player == False:
    # set player to True
    player = input("Stone...Paper...Scissors==>")
    
    print("Your opponent had",pc)

    if player == pc:
        print("Tie!")
    elif player == "Stone":
        if pc == "Paper":
            print("You Lose!",pc,"covers",player)
        else:
            print("You Win!",player,"smashes",pc)
    elif player == "Paper":
        if pc == "Scissors":
            print("You Lose!",pc,"cuts",player)
        else:
            print("You Win!",player,"covers",pc)
    elif player == "Scissors":
        if pc == "Stone":
            print("You Lose!",pc,"smashes",player)
        else:
            print("You Win!",player,"cuts",pc)       
    else:
        print("Invalid Input")

    player = False
    pc = t[randint(0,2)] 