#####################################################             Assignment 2:              #############################################################################
  """ Using the global variables provided in this template, complete the definitions of the functions declared below"""

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


# REQ 1: (Done) Function that counts the number of times a parameter (pNumber) appears in the list of numbers.
def countExistence(pNumber):                                   # Declare a function called countExistence that passes a parameter, pNumber, through the definition
    numberOfAppearances = 0                                    # Initialize numberOfAppearances as 0
    for item in listOfNumbers:                                 # Go through each number in the list of numbers and... 
        if item == pNumber:                                    #    ... If a number is equivalent to the input value... 
            numberOfAppearances = listOfNumbers.count(item)    #    ... then numberOfAppearances updates to the number of times the value appears in the list 
    return numberOfAppearances                                 # Return the value of numberOfAppearances
  
# Note: listOfNumbers.count(item) is a function inherent to lists in Python. 
  

# Function that counts how many odd numbers are in even indices within the listOfNumbers
def countOddNumbersInEvenIndices():
    response = 0                                    
    for itemindex in range(len(listOfNumbers)):     
        if itemindex%2 == 0:                        
            if listOfNumbers[itemindex]%2 == 1:     
                response += 1                       
    return response


# Function that retrieves the name of the oldest colleague in the listOfColleagues
def getNameOfOldestColleague():
    oldestPerson = listOfColleagues[0]                 
    for friend in listOfColleagues:                    
        if friend['age'] > oldestPerson['age']:        
            oldestPerson = friend                      
    return oldestPerson['name']                        


# Function that checks if a colleague exists in the listOfColleagues, based on an input name.
def checkColleagueExistence(pName):
    for friend in listOfColleagues:         
        if friend['name'] == pName:         
            return True                     
    return False                            

# Function that calculates the average age of those colleagues who have a greater or equal income to
#  a value input as a parameter
def calculateColleaguesAverage(pIncome):
    sum = 0.0                                   
    count = 0                                   
    average = 0.0                               
    for friend in listOfColleagues:             
        if friend['income'] >= pIncome:         
            sum = sum + friend['age']           
            count += 1                          
    average = sum/count                         
    return average

#  REQ 3: (Done) Delete an input colleague's name
def removeColleague(pName):                       # Declare a function called removeColleague that accepts an input parameter pName 
    responseAge = 0                               # Initialize the response age as 0; allows variability with output message (see below) 
    for friend in listOfColleagues:               # For each individual in the list...
        if friend['name'] == pName:               #   ... if the friend's name is the same as the input value....
            responseAge = friend['age']           #   ... responseAge updates the the value of the friend's age and....
            listOfColleagues.remove(friend)       #   ... the friend is removed from the list. 
    return responseAge                            # Return the value of the response age. 

#  REQ 2: (Done) Return the most repeated number in the list of numbers.
def findMostRepeatedNumbers():                            # Declare a function called findMostRepeatedNumbers; does not accept input values. 
    mostRepeatedNumber = {'integer': 0, 'count': 0}       # Create a dictionary called mostRepeatedNumber that stores integer and count.
    tally = 0                                             # Initialize tally as 0 
    for item in listOfNumbers:                            # For each item in the list...
        tally = listOfNumbers.count(item)                 #   ... tally updates to the number of times the item is contained within the list.
        if tally > mostRepeatedNumber['count']:           #   If the tally value is larger than the value of count as contained within the dictionary mostRepeatedNumber...
            mostRepeatedNumber['integer'] = item          #     ... then update 'integer' within the dictionary mostRepeatedNumber to reflect the item and...
            mostRepeatedNumber['count'] = tally           #     ... update 'count' within the dictionary to reflect the number of times the item appears 
    return mostRepeatedNumber['integer']                  # Return the value of 'integer' contained within the dictionary mostRepeatedNumber 

"""Function calls"""

function1Input = 5
function4Input = "Alexander"
function5Input = 500
function6Input = "Alexander"

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
function6 = removeColleague(function6Input)
function7 = findMostRepeatedNumbers()

message = "Our results are:\n"
message = message + "1) The number: " + str(function1Input) + " appears " + str(function1) + " times in the list\n"                 # REQ 1: DONE
message = message + "2) The number of odd numbers in even indices is: " + str(function2) + "\n"
message = message + "3) The oldest colleague is " + str(function3) + "\n"

if function4 is True:
    message = message + "4) Your colleague: "+function4Input+ " exists in the list\n"
else:
    message = message + "4) Your colleague: "+function4Input+ " does not exist in the list\n"

message = message + "5) The average age is: " + str(function5) + " for those colleagues whose income is greater or equal than " + str(function5Input) + ".\n"

if function6 != 0:
    message = message + "6) Your colleague, " + function6Input + ", who is " + str(function6) + " years-old, was successfully removed.\n"           # REQ 3: DONE
else:
    message = message + "6) The colleague was not removed, as s/he does not exist in the list.\n"

if function7 != 0:
    message = message + "7) The most repeated number in the list of numbers is " + str(function7) + "\n"                                            # REQ 2: DONE

print(message)
