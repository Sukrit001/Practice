print("""\nCalculator
==========""")

while True:

    first_number = 0
    secound_number = 0
    operation = ("")

    number_type = input("\nWhat type of numbers are you going to be using, whole or decimals? ")
    
    if number_type == "whole":
        first_number = int(input("First number "))
        secound_number = int(input("secound number "))
        operation = input("What operation whould you like to do? ")

        

    if number_type == "decimals":
        first_number = float(input("First number "))
        secound_number = float(input("Secound number "))
        operation = input("What operation whould you like to do? ")
    
    repet = input("Would you like to do another equastion? ")

    if repet == "No":
        print("Thank you for using the cal. ")
        break
        


    
        
    