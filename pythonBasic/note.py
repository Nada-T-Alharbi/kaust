
#to print decimal and intergger number and String
#Numbers with a decimal point belong to a class called float
print(100)#int
print("Hello world")#string
print(3.14)#decimal

#operators and operands
print(100+200)#addation opreater 
print(100-200)#sub opreater 
print(100*200)#multi opreater 
print(100/200)#devion opreater 
print(10//3)#devion to take the remander opreater 
print(10%3) #giving the remander
print(4**2)#like say 4^2
#python follow the normal step of opration in math


#Function call
#take in arguments and return the output allowes one value
print(sub(square(3),square(1+1)))
#the data type 
#type : if you dont know the type it will return the type
print(type(100))
#Double quoted strings can contain single quotes inside them, as in "Bruce's beard", and single quoted strings can have double quotes inside them, as in 'The knights who say "Ni!"'. Strings enclosed with three occurrences of either quote symbol are called triple quoted strings. They can contain either single or double quotes:
print('''"Oh no", she exclaimed, "Ben's bike is broken!"''')

print("""This message will span
several lines
of the text.""")#the triple quoted mark 

#Type Conversion function 
print(3.14, int(3.14))
print("2345", int("2345"))    
#print(int("23bottles"))#will get an error
print(str(17))
val=50+19
print("the value is "+str(val))

#Variable : evry varible have name and value
message ="hello"
print(message)
#overwrite varible 
x=5
print(x)
x=10
print(x)#Reassignment
#python Python is called case-sensitive
#take pictue of keywords
#update varible 
x = 6        # initialize x
print(x)
x = x + 1    # update x
print(x)
#increment and decrement
x = 6        # initialize x
print(x)
x += 3       # increment x by 3; same as x = x + 3
print(x)
x -= 1       # decrement x by 1
print(x)
#what is th hard code : Writing the answer directly in the code rather than having the program compute the answer

#input
n = input("Please enter your name: ")#alowes return string
print("Hello", n)

#to take int
str_seconds = input("Please enter the number of seconds you wish to convert")
total_secs = int(str_seconds)
#trutle
import turtle             # allows us to use the turtles library
wn = turtle.Screen()      # creates a graphics window
alex = turtle.Turtle()    # create a turtle named alex
alex.forward(150)         # tell alex to move forward by 150 units
alex.left(90)             # turn by 90 degrees
alex.forward(75)          # complete the second side of a rectangle

#loop
for _ in range(3):#the python space sencitive here the fpr loop and the for name which here is _ then how many times
    print("This line will execute three times")
    print("This line will also execute three times")
    

#random
#randrange : giving a random number between (include,exclsive)
import random

prob = random.random()
print(prob)

diceThrow = random.randrange(1,7)       # return an int, one of 1,2,3,4,5,6
print(diceThrow)


#Erros
#syntax erroes : in what you write
print("Hello World!"
#Run time errors : These occur when the interpreter is able to parse the program. 
print(3/0)#illge opration 

#Semantic Errors : the program run but giving wrong answer
print("one hale as percentage is",1/2)#here so the correct is multi by 100
