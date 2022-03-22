

#///////////////////////////////////////////////////////





#       // name and age //
"""
name = input("Enter your name:")
age = input("Enter your age:")

print("Hello "+ name + "! are you? " + age)
"""
#///////////////////////////////////////////////////////





#       // cauculator //
"""
num1 = input("enter a number: ")
num2 = input("enter another number: ")
result = float(num1) + float(num2)                 # int = no fraction // float = any number// function get
print(result)

                                                    #// str(mynumber) + string

"""

#///////////////////////////////////////////////////////






#       // mad libs game //

"""
color = input("Enter a color; ")
plural_noun = input("Enter a plural noun; ")
celebrity = input("Enter a celebrity; ")
print("roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)
"""

#///////////////////////////////////////////////////////

#           // introduction to lists //
"""
friends = ["Kevin", "Karen", "Jim", "oscar", "Toby"]                            # 0, 1 , 2//// -3, -2, -3
friends[1] = "Mike"                                                            #modify only one name

print(friends[1:3])
"""
#///////////////////////////////////////////////////////




#       // Lists Functions //

"""
ucky_numbers = [8, 4, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]

#friends.extend(lucky_numbers)                                          # add list to the end of a list
#friends.append("creed")                                                #add element to the end of a list
#friends.insert(1,"Kelly" )                   #index, element           #add element to the middle of a list
#friends.remove("Jim")                                                  #remove chosen element
#friends.clear()                                                        #clear every element in the list
#friends.pop()                                                          #remove chosen last element
#print(friends.index("Oscar"))                                          #find location of chosen elemnt
#print(friends.count("Jim"))                                            #how many times elemt exists
#friends.sort()                                                         #put it in alphabetical order
#lucky_numbers.reverse()                                                #Reverse list elemnts orther
#friends2 = friends.copy()                                              #copy list elemnts to new list


print(friends)
print(lucky_numbers)
"""


#///////////////////////////////////////////////////////




#       // Tuples //
"""
coordinates = (4, 5)                                     #cannot change  // list [] Tuples ()
print(coordinates[1])
"""
#///////////////////////////////////////////////////////




#       // Functions //

"""
def say_hi(name, age):                                           #function
    print("Hello " + name + "you are" + age)

say_hi("Steve", " 50")                                           #calling function

"""
#//////////////////////////////////////






#           // return statement //

"""

def cube(num):
    return num*num*num                                                        #  // give value back to be printable
                                                                            #  // get information back from the Functions
result = cube(4)                                                               #  // no code after return statement is interpreted
print(result)

"""

#//////////////////////////////////////





#       // if stetements  //

"""
is_male = True
is_tall = True


if is_male or is_tall:                                     # Varieble True or False
    print("you are a male or tall ")                       # union // can be one or the orther
else:                                                      # If orriginal variable flase then execute new action
    print("You are not a male nor tall ")

"""
"""

if is_male and is_tall:                                     #both must be true to action continue
    print("you are a tall male ")
else:
    print("you are either not male or tall")

"""
"""                                                        # put " : " in the end of the variable line
    print("You are a tall woman")
else:
    print("you are either not male or tall")

"""

#//////////////////////////////////////





#       // If Statements & Comparisons //                 uses of if Statements // Comparisons == is equal values != not equal

"""

def max_num(num1, num2, num3) :                                       #crete funcion to subtitute values
    if num1 >= num2 and num1 >= num3 :
        return num1
    elif num2 >= num1 and num2 >= num3 :                            #if two is biger then 3 and 1 // can only be tru or False
        return num2
    else:
        return num3                                                 #exclusion leaves num3

print(max_num(7,3, 5))                                             # subtitute values and run program // return means give as function values

"""

#//////////////////////////////////////



#           // Building a better Calculator //

"""

num1 = float(input("enter first number: "))   #convert string in a number value
op = input("enter operation: ")
num2 = float(input("enter seccond number: "))


if op == "+" :
    print(num1 + num2)

elif op == "-" :
    print(num1 - num2)

elif op == "/" :
    print(num1 / num2)

elif op == "*" :
    print(num1 * num2)

else:
    print("invalid operator <>")


"""

#//////////////////////////////////////



#   // Dictionaries //

"""

monthConversins = {
    "Jan": "January",                                      # key: Vallue
    "Feb": "Febwary",                                       #aways use unique keys
    "Mar": "March",



}

print(monthConversins["Jan"])                               #     gets value related to the key in the dictionary
print(monthConversins.get("Luv", "Not found :( "))          #    .get makes new not found value

"""

#//////////////////////////////////////



#       // While Loops //

"""

i = 1
while i <= 10:
    print(i)
    i = i + 1                                     #or += 1

print("Done with loop: ")

"""

#//////////////////////////////////////


#       // Guessing Game //


"""
secret_word = "jade"
guess = ""

while guess != secret_word:
    guess = input("Enter guess: ")

print("Nice")

"""

#// with guess count//

"""

secret_word = "jade"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False


while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True


if out_of_guesses:
    print("you Lose ")
else:
    print("You Win ")


"""


#//////////////////////////////////////


#                          // For Loop //

"""

for letter in " coding ":                   #stores every value in a diferrent line // letters
    print(letter)


"""
#////////////////////////////////////////////////
"""

friends = ["Jim", "Karen", "Kevin"]


len(friends)
for index in range(len(friends)):       #not including 10
    print(friends[index])

"""
"""

friends = ["Jim", "Karen", "Kevin"]

for index in range(5):
    if index == 0:
        print("first iteration")
    else:
        print("Not first")


"""


#       // Exponent function //

"""

def raise_to(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raise_to(2, 3))

"""

#////////////////////////////////////////////////


#       // 2D Lists & Nested Loops //                "  listas de listas  "

"""

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]

]



for row in number_grid:
    for col in row:
        print(col)

"""

#////////////////////////////////////////////////



#       // Basic Traslator //

"""

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                tranlation = tranlation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("enter a phrase: ")))

"""

#////////////////////////////////////////////////


#       // coments //


#multiple lines

"""
nothing inside this gets used... // interprited

"""

#single line is like this use hashtag


#////////////////////////////////////////////////


#       // Try Exept //


"""

try:
    awnser = 10/0
    number = int(input("enter a number: "))       #convert into integer
    print(number)
except ValueError:
    print("Invalid input!")
except ZeroDivisionError as err:
    print(err)


"""


#////////////////////////////////////////////////

"""
open("Reading_text.txt", "r")           # r = read, w = write, a = append (write in the back), r+ read and write

"""
"""

employee_file = open("employee.txt", "r")           #open file

for employee in employee_file.readlines():
    print(employee)                       #print all lines


employee_file.close()                   #close file


"""

#////////////////////////////////////////////////
#       // Writing Files  //


"""
employee_file = open("employee.txt")        #printed all lines
print(employee_file.read())
employee_file.close()

"""
"""

employee_file = open("employee1.txt", "w")  #append   // new name creates new file

employee_file.write("\nJoaca")              #escape Character \n use new line

employee_file.close()


"""

#////////////////////////////////////////////////


#       // Modules and Pip  //            import a .py file

"""
import random

feer_in_mile = 5280
meters_in_a_kilomiter = 1000
beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Starr"]



def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(num):
    return random.randint(1, num)
"""

# in the other file: ->
"""
import tut3                 #Impoted variables from this file // make acesseble
print(tut3.roll_dice(6))       #printed using a function present in this file



"""

#////////////////////////////////////////////////

#       // Classes & Objects  //

"""

#// in file //


class Student:   #desines what a student is // template

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name       #name = name passes in function
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation



"""


"""

from Student import Student

student1 = Student("jim","Business", 3.1, False)
student2 = Student("Pam","Qrt", 3.5, True)


print(student2.name)            # acess student data type

"""


#////////////////////////////////////////////////


#       // Object Functions //        Functions inside os classes

"""
from Student import Student          #in Student.py file // code

class Student:   #desines what a student is // templateS
    
    def __init__(self, name, major, gpa):
        self.name = name       #name = name passes in function
        self.major = major
        self.gpa = gpa
    
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

"""
"""

student1 = Student("jim","Business", 3.8)
student2 = Student("Pam","Qrt", 3.4)


print(student1.on_honor_roll())

"""

#////////////////////////////////////////////////


#       //  inheritance //

""" #in ChineseChef

from Chef import Chef

class ChineseChef(Chef):   #makes all functions inheretaded to new class

    def make_special_dish(self)                 # // Overwrites new class making special dish
        print("The chef makes orange chiken")

    def make_fried_rice(self):
        print("the chef makes fried rice")


"""
"""  #      In Chef
class Chef:

    def make_chicken(self):
        print("The chef makes a chiken")
    
    def make_salad(self):
        print("The chef makes a salad")

    def make_special_dish(self):
        print("the chef makes a special dish")

"""
"""


from Chef import Chef
from ChineseChef import ChineseChef

myChineseChef = ChineseChef()
myChineseChef.make_special_dish()



"""


Bird = ['ian', 'cacau']

nice = Bird[0]

print(nice)












#//////////////////////////////////////
