 
#       // Code Flexibility  //

"""

#solution 1

list_of_words = ["hello", "yes", "goodbye", "last", "hello"]

print(list_of_words[0] + "," + list_of_words[1] + "," + list_of_words[2] + "," + list_of_words[3])

#if you want to change this to "." you need to manualy change it// also when you simply add a word thbe code falls apart

print(list_of_words[0] + "." + list_of_words[1] + "." + list_of_words[2] + "." + list_of_words[3])
#manualy changing to "." //  not a good desingn

"""

#/////////////////////////////////////////////////
"""

# malleable list
#solution 2

list_of_words = ["hello", "yes", "goodbye", "last", "hello"]
to_print = ""

for i in range(len(list_of_words)):
    to_print += list_of_words[i]
    if i != len(list_of_words) - 1:
        to_print += ","

print(to_print)
print(len(list_of_words))

"""
#//////////////////////////////////////////////////

#solution 3

"""
#simplfy

list_of_words = ["hello", "yes", "goodbye", "last"]
print(",".join(list_of_words))          

"""
#//////////////////////////////////////////////////
"""
#solution 4
#make it better

Delimeter = ","
list_of_words = ["hello", "yes", "goodbye", "last"]
print(Delimeter.join(list_of_words))

"""

#       // Guessing game // numbers under and over

"""
guess = 1
while True:
    num = input("Please guess the number (between 0-100): ")
    try:
        num = int(num)
    except:
        print("Invalid Number, please try again.")

    if num < 45:
        print("Your guess was under.")
    elif num > 45:
        print("Your guess was over.")
    else:
        break

guess += 1

print(f"You guessed in {guess} guesses")

"""

#//////////////////////////////////////////////////


























# +++++++++++++++++++++++++++++++++++++++++       //        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
