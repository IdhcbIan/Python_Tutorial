from queue import Queue

# -------------------------------------   // Basic concepts revision  //  -----------------------------------------------------------------

#Tutorial // https: // www.youtube.com/watch?v = sxTmJE4k0ho &list = WL&index = 4&t = 19881s
#tech with tim // the complte python tutorial

#           // for loop  //               only run a certain number of times
"""
for x in range(0, 10, 1):   # start, stop, step
    print(x)



"""
#///////////////////////////////////////////
#          // while loops //        run until the condition becomes false,
"""
while conditon = True:
    do this
"""

"""
loop = True

while loop == True:                        # will loop until varialble = False
    name = input("Insert something: ")     # sets input
    if name == "stop":                     # in input == set word then turn variable false
        loop = False                        
        break                               #loop brake in the next run the false variable will make the code stop looping

"""

#///////////////////////////////////////////////////////

#       // Iteratin by item  //
"""
fruits = ['aples', 'pairs', 'strawberies']


#for x in range(0, 10):
#    print(x)



for fruit in fruits:        #runs the number of times in the items
    print(fruit)

"""
#///////////////////////////////////////////////////////


#           // Using .count() and .find() //

"""
#methods to be used in strings

string = "hello"

#print(string.find('l'))     #sertch for the position of l 0,1,2

print(string.count('l'))     #counts th number of c the specific character that you have inserted

"""
#///////////////////////////////////////////////////////


#       //  Optional Parameters //

"""
#basic function
def func(x):
    print(x)

func('hello')
"""

"""
def func(x='3', text='t'):      #create defalt values if nothing is input
    print(x)
    if text == "t":
        print("text is t")
    else:
        print("text is not t")

func()

"""



#---------------------------------------------- //  Object oriented programing  // ------------------------------------------------------






"""
#use the help python function

help(int)

#Gives out all methods of the class integer
"""

#/////////////////////////////////////////////////////



#       //  Optional parameters  //  
"""
Numb = int(input("Square a number:")) #makes input a number
def func(Numb=2):
    return Numb **2          #return makes func(5) = value

call = func(Numb)
print(call)
"""
"""

def func(x=2):       #is no parameter is given default function value to 2
    return x ** 2  


call = func()
print(call)

"""
"""

def func(word="ten", frequnecy=1):    #defaut times frequency is repeated and the word
    print(word*frequnecy)

call = func()    #when calling withought giving parameters 

"""
#/////////////////////////////////////////////////////


#               // Remembering Classes  //

"""

class dog(object):
    def __init__(self, name):   #just creates the dog object // With the name parameter creates new info to be passed
        self.name = name        #self =  instance = tim, fred // Belongs to the instance of
        

    def speak(self):      #method
        print("hi i am", self.name)   #creates a function in this class, something you can call the dog to do

 
tim = dog("Tim")               #something that automaticly fires as you create a new object in the class
fred = dog("Fred")              #instance of type dog// Creates new object of type dog
tim.speak()                     # When calling the function needs to specify .name
fred.speak()

"""

#//////////////////////////////////////////////////////////////////////



"""
class person(object):
    population = 50
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def getPopulation(cls):
        return cls.population

    @staticmethod
    def isAdult(age):
        return age >= 18

    def display(self):
        print(self.name, "is", self.age, "years old")

newPerson = person("tim", 10)

print(person.getPopulation())
"""


#             // Inheritance  //


"""

class dog(object):                                      #general class
    def __init__(self, name, age):
        self.name = name  
        self.age = age

    def speak(self):
        print("hi i am", self.name, 'and i am', self.age, 'years old')

    def talk(self):
        print('Bark!')
         



class cat(dog):
    def __init__(self, name, age, color):    #when calling cat
        super().__init__(name, age)          #calls dog methods   super class is dog
        self.color = color

    def talk(self):                            #overwrites the dog method talk()
        print('Meow!')



haku = cat("haku", 5 ,"blue")                 #calls class
haku.speak()                                  #gets speak method from dog  class
haku.talk()

cacau = dog("cacau", 11)
cacau.speak()
cacau.talk()                                  # in the dog class still barks



"""


#//////////////////////////////////////////////////////////////////////




#       // Overloading defaut python mwthods  // 

"""

class point():                          #how to make operations to new tipes of objects
    def __init__(self, x=0, y=0):      #initiate classes with optional parameters
        self.x = x                     #makes the instance of x a numerical value of x
        self.y = y                    
        self.coords = (self.x, self.y)      
                    #makes function move to the coordinates
    def move(self, x, y):            
        self.x += x
        self.y += y
    
    def __add__(self, p):         #Describes the operation in this case the sum operation
        return point(self.x + p.x, self.y +p.y)  #Returns value of additon the other point

    def __sub__(self, p):         #creates a method that makes any intance of the class do something
        return point(self.x - p.x, self.y - p.y)
    
    def __mul__(self, p):         
        return self.x * p.x + self.y * p.y

    def __str__(self):            #make sthe operation an actial text string
        return "(" +str(self.x) + "," + str(self.y) + ")"



p1 = point(3, 4)  
p2 = point(3, 2)
p3 = point(1, 3)
p4 = point(0, 1)
p5 = p1 + p2

print(p5)
"""

#///////////////////////////////////////////////////////////



#      //  Static methods and Class method  //

"""

class Dog:       
    dogs = []       #create a list  // in not especific to a instance (object of that class)
    xc = 5          #crates a variable that will aways be used

    def __init__(self, name):    
        self.name = name
        self.dogs.append(self)    #appends every dog object in the list dogs

        #decorators // special tipe of methods
    @classmethod   
    def num_dogs(cls):   #cls = name of the class makes possible to call the class on the name of the class not in a specific instance of it
        return len(cls.dogs)

    @staticmethod    #no need for class name, or self and no parameters are needed
    def bark(n):     #cannot use self or even class variables,,, usefull when used as normal functions but organised inside a class
        #barks n times       #also usefull when importing functions from another file, as you can just use classname.method and it will work with no instance
        for _ in range(n):
            print("bark!")


tim = Dog("Tim")
jim = Dog ("jim")



#print(Dog.num_dogs())   #gives out 0 // you can call in the name of the clas. not in an specific intance of it

#Dog.bark(5)   #call a method of the class withoght needing a instance or abject

"""


#///////////////////////////////////////////////////////////




#            //  Private and public classes  //

"""

class _private:     #the underscore in the front of the class name to make private// to humans
    def __init__(self, name):
        self.name = name

class notPrivate:
    def __init__(self, name):
        self.name = name
        self.priv = _private(name)

    def _display(self):
        print("hello")

    def display(self):
        print("hi")





#------------------------------------
#in the other file
#from inter_tut import notPrivate   #import file class
#test = notPrivate("tim")           #calls function
#test.display()                     #displat the test variable
#    or
#test._display()                    #can import even is method is private, because the underscore is only a way of sinalizing not really making it private
#-----------------------------------


"""









#----------------------------------------------------// Intermidiate Tutorial  //-------------------------------------------------------------------




#       // Map Function  //


"""
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def func(x):
    return x**x


newList = []

for x in li:
    newList.append(func(x))


print(newList)
 

#print(list(map(func, li)))     #simplifying    input two thing, a function and a list

#print([func(x) for x in])    #or another option   // makes function for every item in list
print([func(x) for x in li if x%2 == 0])      #olny for the even values of x

"""
#////////////////////////////////////////////////////////////////////



#       // Filter Function  //


"""
def add7(x):
    return x+7


def isOdd(x):
    return x%2 != 0     #filters all odd number

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


b = list(filter(isOdd, a))     # appends oll the odds numbers to the b list, that is empty

c = list(map(add7, b))   #funtion and list  // does something to every item of the list, in this case adds 7

print(a)

print(b)

print(c)
"""

#----------------------// Another Example //-------------------------

"""
# list of alphabets
alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels


def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(alphabet in vowels):
        return True
    else:
        return False


filteredVowels = filter(filterVowels, alphabets)

print('The filtered vowels are:')
for vowel in filteredVowels:
    print(vowel)
"""

#------------------------------------------------

#       // Test  //

"""
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def FilterEven(a):
    Even = [2, 4, 6, 8, 10]

    if (a in Even):
        return True
    else:
        return False


b = list(filter(FilterEven, a))

print(b)

"""
#-----------------------------------------------



#//////////////////////////////////////////////////////////




#       // Lamda Tutorial //         
#anonymous function

"""
def func(x):
    return x+5


print(func(2))
#prints 7


func2 = lambda x: x+5    #anonymous function  // can be used inside of others functions

print(func2(3))
#prints 8
"""


"""
def func(x):
    func2 = lambda x: x+5    #makes operation in x and makes result func2
    return func2(x) + 10     #  gets previous operation value makes new operation



func3 = lambda x,y:x+y     #can also work with more than one parameter or
print(func3(5, 5))

#prints 18
"""
"""

a = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

newList = list(map(lambda x: x+5, a))   # map: does the operation for everu item of a list,,, 
 #and the lambda makes the function inside the map function itself,,
# the list makes the output also a list,,, and the input was the given list a`
#also works with the filter function// Remeber x%2 sees is x is divisible by 2
print(newList)   #calls function
"""



#//////////////////////////////////////////////////////



#       //  Introduction To Colections  //      // Used to manage and count data structures...

"""

import collections
from collections import Counter      #importing module

#containers
    #list
    #set
    #dict
    #tuple

#types
    #counter  <- this tutotrial
    #deque
    #named 
    #named tuple
    
#----------------------

c = Counter("gallad")
print(c)
c = Counter(["a", "b", "c", "c"])
print(c)
c = Counter({"a":1, "b":2})
print(c)
c = Counter(cats=4, dogs=7)



print(c["cats"])   #prints 4, because is the direct value of cats

print("")          #dooes not gives error back

#----------------------------------------------------------------

c = Counter("gallad")
print(c)
c = Counter(["a", "b", "c", "c"])
print(c)
e = Counter({"a": 1, "b": 2})
print(c)
d = Counter(cats=4, dogs=7)


#print(list(c.elements()))         # print in the list of the item repeated that number of times

print(c.most_common(2))           #number os most common elements // returns the number of times the element apears

#------------------------------------------


c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(["a", "b", "b", "c"])

#c.subtract(d)  # subtract 1 from every element
#print(c)
#c.update(d)    # Updates the c list replacing with the d list
#print(c)
#c.clear()      # Clear the list
#print(c)

# You can also makes operations

#print(c+d)    # Collects all the elemnts
#print(c-d)    # Subtracts the firt element list 
#print()

#print(c & d)    # Intesection
#print(c | d)    # Union // Max Element  // takes maximum element 

"""

#//////////////////////////////////////////////////////


#       // Named Tuple  //

"""

import collections
from collections import namedtuple   #import function

#------------------------------------------
Point = namedtuple("point", "x y z")

newP = Point(3, 4, 5)

print(newP)

#prints(point(x=3, y=4, z=5))    // substitutes the the parameters
#-----------------------------------------

#   Using in Lists

Point = namedtuple("Point", ['x', 'y', 'z'])

newP = Point(3,4,5)
print(newP)

#----------------------------------------
#    Using methods

Point = namedtuple("Point", ['x', 'y', 'z'])

newP = Point(3, 4, 5)
print(newP.x, newP.y, newP.z)   # Gets the items by it self
print(newP[0])                  #gets only the certain element
print(newP._asdict())           # Makes every item into a dictionary
print(newP._fields)             #gives a tuple with the fields in it
print(newP._replace(y=6))       # Changes certain element, to use this as a solo function use to create a new tuple

p2 = Point._make(['a', 'b', 'c'])   #grab and assign to the old xyz 
print(p2)
"""

#//////////////////////////////////////////////////////////////////////////////


#       //  Deque  // 

"""

import collections
from collections import deque

d = deque('hello')



#prints //  deque(['h', 'e', 'l', 'l', 'o'])   
#decomposes the word to a new type of data type

d.append('4')           # appends to the end
d.appendleft('5')       # appends to the beginig

print(d)
d.pop()           #removes the last
d.popleft()       #reoves the first
# you can olso give the index of the element to remove it  d.pop(x)
print(d)

d.clear()     # clear the deque
print(d)

d.extend('456')    # adds the decomposed value to the deck
d.extend([1, 2, 3]) # decomposes the list
d.extendleft('hey')   #gets in reverse, because is adding in the reverse orther
print(d)

d.rotate(-1)   #rotates the first element to the back// magnified by the input argument
print(d)

d.rotate(-2)   # rotate the 2 from the front to the back
print(d)


g = deque('nices', maxlen=5)  #removes the first element and adds one to the back
print(g)                       #max len is not writeble
g.append('4')     # replaces with the new input element
print(g)

"""

#////////////////////////////////////////////////////////////////////////////










#-------------------------------------------------------------//  Expert Tutorial  //-----------------------------------------------------------------------




#            //  Overview of Python  //  

"""
class Dog:
    def __init__(self):
        self.bark()


# Just works because the file is compiled at runtime
# Not specified stribute, but still works



def make_class(x):  
    class Dog:                      #class inside dunction
        def __init__(self, name):   #can only execute because of the way that python is compiled
            self.name = name  

        def print_value(self):
            print(x)

    
    return Dog

cls = make_class(10)    #returns class itself, not a instance

#print(cls)
#  <class '__main__.make_class.<locals>.Dog'>
#main means it came from the mais module // make class is the name of the function we defined
#// locals is defines whats in the function, and dog says whats in the class
#----------------------

d = cls("Tim")      #makes the cls variable a anctual class
d.print_value()     # and so calls the method on the object
#                   #prints the input value in the class call
#prints value 10


#----------------------------------------

for i in range(11):    #does not includes 10
    def show():        # so 9 * 2 == 0 - 18 
        print(i*2)    #prints all elements in the range

#    show()           # shows all the elements

show()           # Prints 20 the last value of the variable not the elements

#----------------------------------------


import inspect


def func(x):
    if x == 1:
        def rv():
            print("x is equal to 1")

    else:
        def rv():
            print("x is not 1")

    return rv

new_func = func(2)

#new_func()
#print(id(new_func))  #gets memory adress

#print(inspect.getmembers(new_func))   #prints raw info from the function
#print(inspect.getsource(new_func))    # Gets the actual soure code


#---------------------------------

import inspect
from queue import Queue


print(inspect.getsource(Queue))    #gets source code from the module // functios

#---------------------------------

"""

#       //  Dunder/Magic Methods  //       explaining the operations
"""
import inspect


x = [1, 2, 3]
y = [4, 5]

print(x + y)      # Combines two lists apending
print(len(x))     #length of a list
print(x * 3)      #print the list 3 times

# the operatins tell the objects how to behave

print(x)    # tells pithon what to print

#---------------------------------

class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person({self.name})'  # shows to the sistem what to inform when asking for an object

    def __mul__(self, x):     # this is a Dunder method
        if type(x) is not int:
            raise Exception("invalid argument must be int")

        self.name = self.name * x

    def __call__(self, y):
        print("call this function", y)  #prints the string with the var

    def __len__(self):
        return len(self.name)

p = Person("Ian")

#print(p)          #prints memory adress location // does not know what to show
#prints // Person(Ian)

#p * 4
#print(p)  #prints name 3 times // string 
#                                                 # implemets the strings or class and make new functionality
print(len(p))                                    # this are the Dunder methods
p(4)
#-------------------------

"""
"""
from queue import Queue
import inspect

#q = Queue()
#print(q)
#print(inspect.getsource(Queue))   #inspects the Queue module



# the data module 

from queue import Queue as q
import inspect


class Queue(q):
    def __repr__(self):
        return f'Queue({self._qsize()})'

    def __add__(self, item):  #maps to a lower level python that implemets the functionality
        self.put(item)



qu = Queue()
qu + 9
qu + 7
print(qu)

"""

#/////////////////////////////////////////////////////////////////


#       // Metaclasses  //


"""
#------------------------
def hello():    # a class creates a class for us
    class Hi:    # But a class is a object itself
        pass      # in this case who created the class object 

    return Hi        # A class defines the rules for an object


#------------------------

class Test:
    pass

#print(Test)
#print(Test())


print(type(Test))
#prints // <class 'type'>  // 

"""
#----------------------

#class Test:
#    pass
"""
# These two things are completely the same... 

Test = type('test', (), {})     # Creates the class
#                   parent class, atributes
print(Test)   # Shows a class
#-------------------------



Test = type('test', (), {'x':5})

t = Test()

print(t.x)    #prints the atribute the class t witch // 5 is the class x atribute


#----------------------

class Foo:
    def show(self):   # Crated a parent class
        print('hi')

    def add_attribute(self):
        self.z = 9

#type(name, basas, attrs)
Test = type('test', (Foo,), {'x': 5})    # inherited the function in the parent class
t = Test()        #make class a variable
t.wy = 'hello'        #creates the instance
t.show()         #Uses the function inherited inside the secundary class
# gives out // hi

t.add_attribute()
print(t.z)
# gives out 9 // inherited the function and called the function in self.z == in this case x.z


#------------------------------------


class Meta(type):
    def __new__(self, class_name, bases, attrs):        #new is called before the init method // modify the way a object is constructed
        print(attrs)

        a = {}  #new atributes
        for name, val in attrs.items():
            if name.startswith('__'):
                a[name] = val
            else:
                a[name.upper()] = val
        print(a)
        return type(class_name, bases, a)


class Dog(metaclass=Meta):
    x = 5
    y = 8

# gives out // {'__module__': '__main__', '__qualname__': 'Dog', 'x': 5, 'y': 8}  //

    def hello(self):
        print('hi')

d = Dog()
print(d.X)   # needs to be Upercase X 
# Gives out 5


#used to modify module class and libwary


#/////////////////////////////////////////////////////
"""

#       //  Decorators  //
"""

#--------------------------------

def func(f):          #accepts a function as a argument
    def wrapper():
        print("started")
        f()                  # the parameter itself makes calls the function
        print("Ended")

    #return wrapper()    #with the braces the function is alredy called
    return wrapper    #store the function in the variable x

#x = func('hello')

def func2():
    print('i am func2')


x = func(func2)   # f will be = to func to, so then it calls f() is calling func2()
print(x)
x()     #calls the function


#---------------------------------------------------------


#def func(f):  
#    def wrapper():
#        print("started")
#        f()                     #calls the passed function in the parameters  
#        print("Ended")
#        print('this is func')  # to make shure is running as func 

#    return wrapper 

def func(f):
    def wrapper(*args, **kwargs):     #handles any amount of arguments even 2 
        print("started")
        rv = f(*args, **kwargs)              #calls the original function           
        print("Ended")
        print('this is func')   
        return rv   

    return wrapper

def func2():
    print('i am func2')


@func                    # == func3 = func(func3)  // puts the name of the function as a parameter for the main function
def func3():
    print('i am func3')

 
@func              #when func4 is called the func function is called with func 4 as the parameter
def func4(x, y):     # the parameter of the function x will still be named x
    print(x)      # when called the func will execute action
    return y


#x = func(func2)    #decorator function
#y = func(func2)
#print(x)
#x()
#y()

#func3 = func(func3)   #makes the decorator func3 to func2
#func2 = func(func2)

#func2()
x = func4(5, 3)   #the func will be acepted but the argument will not be used 
print(x)
#func3()

#-------------------------------

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func()
        total = time.time() - start
        print('time:', total)
        return rv

    return wrapper

@timer
def test():
    for _ in range(1000):
        pass 


@timer
def test2():
    time.sleep(2)


test()
test2()
"""


#///////////////////////////////////////////////////

#Tutorial used: tech with tim // https: // www.youtube.com/watch?v = sxTmJE4k0ho &list = WL&index = 4&t = 19881s

print("hello world")



#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++    //      +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
