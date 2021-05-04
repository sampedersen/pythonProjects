"""Assignment 1:
  Using the global variables provided in this template, complete the definitions of the functions declared below"""

#Imported libraries
import random


###############################################################################################################################################
##################################################  Global Variables  #########################################################################
###############################################################################################################################################

#Q1: How does the random.randint(_,_) work?
""" "random" first identifies the module a function will be called from.
    "randint" then identifies the function being used; in this case, we are generating a random integer.
    This function has a parameter (_,_) that allows users to indicate the upper and lower boundaries
    that the integer will be selected from. 
    The function then returns the generated number. """

#Q2: What is "random" and what is the purpose of using the period (.) before randint?
""" "random" is the name of the module, which includes a set of functions built-into Python.
    The (.) preceding randint opens the module and allows the randomint functino to be
    selected, returning a random number once executed. """

randomNumberA = random.randint(1, 100)
randomNumberB = random.randint(-50, 100)
randomNumberC = random.randint(15, 150)
randomNumberD = random.randint(-13, 1990)
randomNumberE = random.randint(-100, 0)

#Q3: What does the function print(_) do in the next line of code?
""" The print(_) function will form a string of the objects enclosed within the parentheses
    and it will then display (print) it to the console."""

#Q4: What is the purpose of the (+) operator in the next line of code?
""" The (+) operator is acting as a connector, linking strings within the parentheses of the
    print(_) statement to be displayed together. This use of the (+) operator is also known as string concatenation. """

#Q5: What is the purpose of the function str(_) in the next line of code?
""" In order to perform string concatenation, objects within the argument of print(_) must all
    be of a string data type. To make this conversion, str(_) converts the variable from an
    integer data type to a string data type that can then be be printed."""

print("The numbers generated are: " + str(randomNumberA) +" "+ str(randomNumberB) +" "+str(randomNumberC) +" "+ str(randomNumberD) +" "+ str(randomNumberE))

###############################################################################################################################################
################################################  Functions' declaration and definition  ######################################################
###############################################################################################################################################

#Q6: Is the variable largest global or local? Why?
""" This variable is local, since it is being defined within a function.
    While the variable's value is initially set as None, it is reassigned
    later within the function. """

#Function that retrieves the largest number between the random variables
""" TODO: (Completed)""" 
def getLargestRandom():
    largest = randomNumberA
    if largest < randomNumberB:
        largest = randomNumberB
    if largest < randomNumberC:
        largest = randomNumberC
    if largest < randomNumberD:
        largest = randomNumberD
    if largest < randomNumberE:
        largest = randomNumberE
    return largest

#Q7: What does None mean?
""" None is a value used to indicate that a statement does not have a value.
    Since the function needs a placeholder for the variable's value, we can use None until the
    variable is later reassigned a new value."""
  
#Function that retrieves the smallest number between the random variables
""" TODO: (Completed)""" 
def getSmallestRandom():
    smallest = randomNumberA
    if smallest > randomNumberB:
        smallest = randomNumberB
    if smallest > randomNumberC:
        smallest = randomNumberC
    if smallest > randomNumberD:
        smallest = randomNumberD
    if smallest > randomNumberE:
        smallest = randomNumberE
    return smallest

# Q8: What is inputValue? Why is it necessary for the following function?  
""" This function accepts an inputValue as a parameter. When we use a parameter's value/object 
    within the function itself, we use a local variable to pass it through each line."""
  
#Function that retrieves the quantity of random numbers greater and equal than an input value
""" TODO: (Completed)""" 
def countGreaterEqualNumbers(inputValue):
    count = 0
    if randomNumberA >= inputValue:
        count = count + 1
    if randomNumberB >= inputValue:
        count = count + 1
    if randomNumberC >= inputValue:
        count = count + 1
    if randomNumberD >= inputValue:
        count = count + 1
    if randomNumberE >= inputValue:
        count = count + 1
    return count

# Q9: What does return do?
""" The return statement ends the function (no code will be executed following the return).
    It also stores the final result that the function will produce when called."""
  
#Function that retrieves the smallest odd number between the random variables.
#The function returns None if there are no random odd numbers.
""" TODO: (Completed)""" 
def getSmallestOddRandom():
    smallestOdd = None
    if randomNumberA % 2 == 1:
        smallestOdd = randomNumberA
    elif randomNumberB % 2 == 1:
        smallestOdd = randomNumberB
    elif randomNumberC % 2 == 1:
        smallestOdd = randomNumberC
    elif randomNumberD % 2 == 1:
        smallestOdd = randomNumberD
    elif randomNumberE % 2 == 1:
        smallestOdd = randomNumberE
    else:
        return None

    if smallestOdd > randomNumberB and randomNumberB % 2 == 1:
        smallestOdd = randomNumberB
    if smallestOdd > randomNumberC and randomNumberC % 2 == 1:
        smallestOdd = randomNumberC
    if smallestOdd > randomNumberD and randomNumberD % 2 == 1:
        smallestOdd = randomNumberD
    if smallestOdd > randomNumberE and randomNumberE % 2 == 1:
        smallestOdd = randomNumberE

    return smallestOdd


# Function that calculates the average of the random variables.
""" TODO: (Completed)""" 
def calculateAverage():
    average = (randomNumberA + randomNumberB + randomNumberC + randomNumberD + randomNumberE)/5
    return average

###############################################################################################################################################
##############################################################  Function calls  ###############################################################
###############################################################################################################################################

#Variable declared for function 3
randomInput = random.randint(-1000, 1000)

# Q10: What is the difference between declaring, defining, and calling a function?
""" A function is declared by creating it and giving it a name.
    The function is then defined by enlisting a set of instructions that give the function purpose.
    Calling a function will then execute the instructions from within the function's definition."""

function1 = getLargestRandom()
function2 = getSmallestRandom()
function3 = countGreaterEqualNumbers(randomInput)
function4 = getSmallestOddRandom()
function5 = calculateAverage()

message = "Our results are:\n"
message = message + "1) The largest number is: " + str(function1) + "\n"
message = message + "2) The smallest number is: " + str(function2) + "\n"
message = message + "3) There are " + str(function3) + " numbers greater than " + str(randomInput)+ "\n"

if function4 is None:
    message = message + "4) There are not odd numbers \n"
else:
    message = message + "4) The smallest odd number is: " + str(function4) + "\n"

message = message + "5) The average is: " + str(function5)

# Q11: How was the variable message built?
""" The variable "message" is built by concatenating a series of strings together within 
    the print function's argument. Within the argument, the variables of an integer type are also 
    converted to string type."""


print(message)
