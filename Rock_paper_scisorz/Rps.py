import random

value = random.random()
#print(value)



play = input("Rock paper scizors(r,p,s):")

print("")


if play == "r":
    print("You played rock")
if play == "p":
    print("You played paper")
if play == "s":
    print("You played scizors")




#       // computer  //                     //////////////////                  //////////////////              /////////////////////


if value < 0.33:
    print("Computer played rock")
    anwser = "r"

if value > 0.33 and value < 0.66:
    print("Computer played paper")
    anwser = "p"

if value > 0.66:
    print("Computer played sizors")
    anwser = "s"



if anwser != play:
    if anwser == "r":
        if play == "p":
            print("you win!")
        else:
            print("you lose!")
    if anwser == "s":
        if play == "r":
            print("you win!")
        else:
            print("you lose!")
    if anwser == "p":
        if play == "s":
            print("you win!")
        else:
            print("you lose!")
else:
    print("draw")




print("")
print(value)


#//////////////////////////////////////////////////////////////////////////////
