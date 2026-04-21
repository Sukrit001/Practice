import random                   # This imports the random module.

deposited_money = 0             # Thsi makes sure that the deposited money always starts with 0.

print("""Lucky Unicorn  
=============""")               # This is the title.

while True:                     # this while loop makes sure thet the user has put in the correct amount of money or it will keep replaying it.

    deposited_money = float(input("\nHow much money would you like to deposit, min 1 doller and max 10 dollers? "))

    if deposited_money >= 1 and deposited_money <= 10:              # This check that the user input is between 1 to 10
        break
    else:
        print("Please enter an amount between $1 and $10. ")               # This tells the user to input the right amount of money


while deposited_money > 0:               # this while loop makes sure that the user can play many rounds
    play = input("Press Enter to play a round (costs $1), or type 'quit' to stop: ").lower()        # this tells the user what to do if they want to play a round
    animals = random.choice(["zebra", "horse", "donkey", "unicorn"])        # this line randomaly chooses what animal it is
    if play == "":                  # this if make sure that the user pressed enter
        print("")
        deposited_money -= 1        # this line makes it so it takes a doller of the user playes a round
        print("Starting round...")
        print(f"The computer chose {animals}")      # this line tells the user that animal was chosen
        if animals == "zebra":      # these if and elif see what animal was chosen and depending on what the animal is it it gives the user money or not.
            deposited_money += .50
            print("You have won 50 cents.")
            print(f"Your total is ${deposited_money}")
        elif animals == "horse":
            deposited_money += 2
            print("You have won 2 dollars.")
            print(f"Your total is ${deposited_money}")
        elif animals == "donkey":
            print("Unfortunately you have not won anything this round.")
            print(f"Your total is ${deposited_money}")
        elif animals == "unicorn":
            deposited_money += 5
            print("You have won 5 dollars.")
            print(f"Your total is ${deposited_money}")
    

    elif play == "quit":            # this elif is if teh user wants to quit.
        print(f"You have ${deposited_money}")           # this line tells the user how much money thay have
        break
    elif play != "" and play != "quit":             # this elif makes sure teh user press enter or types quit
        print("Please press enter to play a round or type 'quit'.")


print("Thank you for playing.")         # this thanks the player for playing