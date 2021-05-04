"""Assignment 2:
  Using the global variables provided in this template, complete the definitions of the functions declared below"""

# Imported libraries
import random

"""Global Variables"""
listOfNumbers = []
listOfColleagues = []

"""Functions' declaration and definition"""
def initializeListOfNumbers():
    count = 0
    while (count < 20):
        item = random.randint(-1000, 1000)
        listOfNumbers.append(item)
        count = count + 1
        
def initializeListOfColleagues():
    friendOne = {'name': 'Alexander', 'age': 35, 'sex': 'male', 'income': 1500}
    friendTwo = {'name': 'Yingbo', 'age': 32, 'sex': 'male', 'income': 1700}
    friendThree = {'name': 'Mustafa', 'age': 30, 'sex': 'male', 'income': 1200}
    friendFour = {'name': 'Julieth', 'age': 33, 'sex': 'female', 'income': 2500}
    friendFive = {'name': 'Natalia', 'age': 28, 'sex': 'female', 'income': 3000}
    listOfColleagues.append(friendOne)
    listOfColleagues.append(friendTwo)
    listOfColleagues.append(friendThree)
    listOfColleagues.append(friendFour)
    listOfColleagues.append(friendFive)


# Function that counts the number of times an input number (the parameter) is in the listOfNumbers
def countExistence(pNumber):
    response = 0
    # TODO Complete this function
    return response


# Function that counts how many odd numbers are in even indices within the listOfNumbers
def countOddNumbersInEvenIndices():
    response = 0
    # TODO Complete this function
    return response


# Function that retrieves the name of the oldest colleague in the listOfColleagues
def getNameOfOldestColleague():
    response = None
    # TODO Complete this function
    return response


# Function that checks if a colleague exists in the listOfColleagues, based on an input name.
def checkColleagueExistence(pName):
    response = False
    # TODO Complete this function
    return response


# Function that calculates the average age of those colleagues who have a greater or equal income to
# a value input as a parameter
def calculateColleaguesAverage(pIncome):
    response = 0.0
    # TODO Complete this function
    return response


"""Function calls"""

function1Input = 5
function4Input = "Alexander"
function5Input = 500

initializeListOfNumbers()
initializeListOfColleagues()

#We print the original lists so that you can visualize them for this assignment
print("List of generated numbers: " + str(listOfNumbers))
print("List of colleagues: " + str(listOfColleagues))

function1 = countExistence(function1Input)
function2 = countOddNumbersInEvenIndices()
function3 = getNameOfOldestColleague()
function4 = checkColleagueExistence(function4Input)
function5 = calculateColleaguesAverage(function5Input)

message = "Our results are:\n"
message = message + "1) The number: " + str(function1Input) + " exists " + str(function1) + "times\n"
message = message + "2) The number of odd numbers in even indices is: " + str(function2) + "\n"
message = message + "3) The oldest colleague is " + str(function3) + "\n"

if function4 is True:
    message = message + "4) Your colleague: "+function4Input+ " exists in the list\n"
else:
    message = message + "4) Your colleague: "+function4Input+ " does not exist in the list\n"

message = message + "5) The average age is: " + str(function5) + " for those colleagues whose income is greater or equal than " + str(function5Input)

print(message)
