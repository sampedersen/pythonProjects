"""Assignment 1:
  Using the global variables provided in this template, complete the definitions of the functions declared below"""

#Imported libraries
import random


"""Global Variables"""
#Q1: How does the random.randint(_,_) work?
#Q2: What is "random" and what is the purpose of using the period (.) before randint?
randomNumberA = random.randint(1, 100)
randomNumberB = random.randint(-50, 100)
randomNumberC = random.randint(15, 150)
randomNumberD = random.randint(-13, 1990)
randomNumberE = random.randint(-100, 0)

#Q3: What does the function print(_) do in the next line of code?
#Q4: What is the purpose of the (+) operator in the next line of code?
#Q5: What is the purpose of the function str(_) in the next line of code?
print("The numbers generated are: " + str(randomNumberA) +" "+ str(randomNumberB) +" "+str(randomNumberC) +" "+ str(randomNumberD) +" "+ str(randomNumberE))

"""Functions' declaration and definition"""
#Function that retrieves the largest number between the random variables
def getLargestRandom():
    #Q6: Is this variable (largest) global or local? Why?
    largest = None
    #TODO Complete this function
    return None

#Function that retrieves the smallest number between the random variables
def getSmallestRandom():
    #Q7: What does None mean?
    smallest = None
    #TODO Complete this function
    return None

#Function that retrieves the quantity of random numbers greater and equal than an input value
def countGreaterEqualNumbers(inputValue):
    # Q8: What is inputValue? Why is it necessary for this function?
    count = None
    #TODO Complete this function
    return None

#Function that retrieves the smallest odd number between the random variables.
#The function returns None if there are no random odd numbers.
def getSmallestOddRandom():
    smallestOdd = None
    #TODO Complete this function

    # Q9: What does return do?
    return None


# Function that calculates the average of the random variables.
def calculateAverage():
    average = None
    # TODO Complete this function
    return None

"""Function calls"""

#Variable declared for function 3
randomInput = random.randint(-1000, 1000)

# Q10: What is the difference between declaring, defining, and calling a function?
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
print(message)
