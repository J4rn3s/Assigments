#################################################################
# File name:CarlosMidterm.py                                    #
# Author: Carlos Lucio Junior                                   #
# Date:06-02-2021                                               #
# Classes:  ITS 220: Programming Languages & Concepts           #
# Instructor: Matthew Loschiavo                                 #
# This is a Midterm                                             #
# Create a game to teach kindergartners how to sum              #
#################################################################


def playNo():
    print("If you do not play you will not get a lollipop. Do you want to play?")
    # Condition if, in case of Negative answer, causing one time loop insisting the kid to play a game#
    play = input("Y/N?")
    play = play.upper()

    return play

def playYes():
    print("Let's do it kiddos!!")

    firstnumber = int(input("Choose a number beween 1 and 9. Please enter your choice now!"))
    secondnumber = int(input("Good job! Now choose another one."))
    result = int(input("Great. Now let's sum both numbers! What is the result?"))
    n = 0

    score = firstnumber + secondnumber
    # print(score) #Used this line for testing purposes#
    # print(result) #Used this line for testing purposes#
    while n != 1:
        if score == result:
            print("You got it and you won a lollipop! High five!")
            n = 1
        else:
            print("")
            result = int(input("Ops, this is not the right answer, try again! What is the result?"))

    return

def prompttoplay():
    print("Today we are going to learn Math! Let's play a game shall we?")
    play = input("Y/N?")
    play = play.upper()  # Here I used the example for correct the lower and upper case letter answer#
    return play

play = prompttoplay()

if play == "N":
    play = playNo()
if play == "Y":
    playYes()

if play != "N" and play != "Y":
    print('You didn\'t answer Y or N')
    #print("You didn't answer Y or N")
    prompttoplay()
else: ## code for X to exit
    print("That is so sad :( ! Good bye!!")
