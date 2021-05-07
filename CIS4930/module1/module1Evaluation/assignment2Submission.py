#####################################################             Assignment 2:              #############################################################################
  """ Using the global variables provided in this template, complete the definitions of the functions declared below"""

# Imported libraries
import random

"""Global Variables"""
# Declare list of numbers and colleagues 
listOfNumbers = []
listOfColleagues = []

"""Functions' declaration and definition"""
def initializeListOfNumbers():
    count = 0
    while (count < 20):
        item = random.randint(-1000, 1000)
        listOfNumbers.append(item)
        count = count + 1
# adding random number to the list of numbers until count = 20

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


#TODO 1. (COMPLETE) Function that counts the number of times an input number (the parameter) is in the listOfNumbers
def countExistence(pNumber):
    response = 0                                # Initialize 
    for item in listOfNumbers:                  # Run through listOfNumbers and apply these rules to each instance (item)
        if item == pNumber:                     # If the instance is equal to the input, we increase out response by 1
            response = response + 1
    return response


#TODO 2. (DONE) Function that counts how many odd numbers are in even indices within the listOfNumbers
def countOddNumbersInEvenIndices():
    response = 0                                    # Take the length of listOfNumbers (ex 20) and evaluate the range (ex 0, 1, ..., 19)
    for itemindex in range(len(listOfNumbers)):     # For each index position in the array:
        if itemindex%2 == 0:                        # If the value of that position is even, continue
            if listOfNumbers[itemindex]%2 == 1:     # Take the value of itemindex and find the number at the position within listOfNumbers
                response += 1                       # If the value at that position is odd, add 1 to the response
    return response


#TODO 3. (DONE) Function that retrieves the name of the oldest colleague in the listOfColleagues
def getNameOfOldestColleague():
    oldestPerson = listOfColleagues[0]                  # Initialize oldestPerson as the first friend (friendOne) in the listOfColleagues
    for friend in listOfColleagues:                     # For each friend in the list, apply these criteria:
        if friend['age'] > oldestPerson['age']:         # If that friend's age is older than the oldest person's age,
            oldestPerson = friend                       # Update the oldest person to that friend
    return oldestPerson['name']                         # Return the updated oldest person's name


#TODO 4. (DONE) Function that checks if a colleague exists in the listOfColleagues, based on an input name.
def checkColleagueExistence(pName):
    for friend in listOfColleagues:         # Run through the listOfColleagues and apply this criteria
        if friend['name'] == pName:         # If the friend's name is equivalent to the input name, return true
            return True                     # If the value is True, the function does not execute the rest of the program
    return False                            # If the if statement was not met, default to false.

#TODO 5. (DONE) Function that calculates the average age of those colleagues who have a greater or equal income to
#                a value input as a parameter
def calculateColleaguesAverage(pIncome):
    sum = 0.0                                   # Variable that stores the value of each person's age
    count = 0                                   # Variable that stores the number of people included in the average
    average = 0.0                               # Initial value of average variable; used later
    for friend in listOfColleagues:             # For each object in the listOfColleagues, apply this criteria
        if friend['income'] >= pIncome:         # If the value of 'income' is greater or equal to the input value,
            sum = sum + friend['age']           # then add the value of their age to the sum variable
            count += 1                          # And also increase the count by one
    average = sum/count                         # Divide the total age by number of people
    return average


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
message = message + "1) The number: " + str(function1Input) + " exists " + str(function1) + " times\n"
message = message + "2) The number of odd numbers in even indices is: " + str(function2) + "\n"
message = message + "3) The oldest colleague is " + str(function3) + "\n"

if function4 is True:
    message = message + "4) Your colleague: "+function4Input+ " exists in the list\n"
else:
    message = message + "4) Your colleague: "+function4Input+ " does not exist in the list\n"

message = message + "5) The average age is: " + str(function5) + " for those colleagues whose income is greater or equal than " + str(function5Input)

print(message)
