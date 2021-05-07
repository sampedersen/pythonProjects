#####################################################             Module 2 - Assignment 1:              #############################################################################
  """ Using the global variables provided in this template, complete the definitions of the functions declared below"""

# Imported libraries
import random

"""Global Variables"""
listOfNumbers = [15, 15]          # Note: Initialize with duplicated values to test function 
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


# REQ 1: (Done) *Recursive* function that counts the number of times a parameter (pNumber) appears in the list of numbers.
def countExistenceRecursion(pNumber, index=0, count=0):              # Define countExistenceRecursion; accepts parameters pNumber, index, and count. Index & count initialize to 0.
    if index == len(listOfNumbers):                                  # Base function: if we have reached the end of the list....
        return count                                                 #    ... then return the number of times the input (pNumber) was counted
    else:                                                            # Otherwise (recursion)...
        if listOfNumbers[index] == pNumber:                          #    ... if number at index position is equal to the input (pNumber)...
            count += 1                                               #            ... then update the count value by +1
        index +=1                                                    #    No matter what, update the index value by +1 and...
        return countExistenceRecursion(pNumber, index, count)        #    ... run thru recursion until base function is true.
  

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

#  Delete an input colleague's name
def removeColleague(pName):                       
    responseAge = 0                               
    for friend in listOfColleagues:               
        if friend['name'] == pName:               
            responseAge = friend['age']           
            listOfColleagues.remove(friend)       
    return responseAge                            

#  REQ 2: (Done:) *Recursive* function that returns the most repeated number in the list of numbers.
def findMostRepeatedNumbersRecursion(mostRepeated=0, maxAppearances=0, index=0):        # Define function; accepts variables mostRepeated, maxAppearances, & index, all initialized as 0.
    if index == len(listOfNumbers):                                                     # Base function: if we've reached the end of the list....
        return mostRepeated                                                             #    ... return the value of mostRepeated
    else:                                                                               # Otherwise (recursion):
        pNumber = listOfNumbers[index]                                                  #    ... pNumber assigned the value of the number at index position in the list of numbers
        if countExistenceRecursion(pNumber) > maxAppearances:                           #    ... if pNumber appears more often than whatever number at index position has appeared,,,
            maxAppearances = countExistenceRecursion(pNumber)                           #         ... then update highest number of appearances to reflect pNumber and...
            mostRepeated = pNumber                                                      #         ... update the most freq number to be pNumber
        index += 1                                                                      #    ... No matter what: increment index +1 and...
        return findMostRepeatedNumbersRecursion(mostRepeated, maxAppearances, index)    #    ... run thru the loop again until the base function is true. 

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

function1 = countExistenceRecursion(function1Input)                         # REQ 1: DONE
function2 = countOddNumbersInEvenIndices()
function3 = getNameOfOldestColleague()
function4 = checkColleagueExistence(function4Input)
function5 = calculateColleaguesAverage(function5Input)
function6 = removeColleague(function6Input)
function7 = findMostRepeatedNumbersRecursion()                              # REQ 2: DONE

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
