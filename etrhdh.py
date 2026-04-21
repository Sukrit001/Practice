import random

animals = random.choice(["zebra", "horse", "donkey", "unicorn"])

print("""Lucky Unicorn
=============""")
deposited_money = 0
while True:

    deposited_money = int(input("\nHow much money would you like to deposit, min $1 and max $10. "))

    if deposited_money >= 1 and deposited_money <= 10:
        play = input("Press Enter to play a round, this will cost $1? ")
        if play == "":
            break
        elif play != "":
            print("Please press enter to play a round.")

    else:
        print("Plese try again and deposit the right amount of money. ")
while True:        
    print("Round starting...")
    print(f"The computer chose {animals}")
    break
