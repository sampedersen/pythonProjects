##################################################################            Tree Class           #################################################################################################


class Tree:
    
    def __init__(self):                                                               # Constructor function; self parameter refers to the (potential) current instance of the class 
        self.root = None                                                              # Initializes root as None 
        self.numberOfElements = 0                                                     # Tree is empty; 0 elements 


        
    def insert(self, pElement):                                                       # Declare an insertion function; self reference variable & pElement input value 
        response = None                                                               # Initialize response as None
        if self.root is None:                                                         # If the instance of the root still returns as None....
            self.root = Node(pElement)                                                #     ... Insert root by running pElement through Node function and...
            response = str(pElement) + " was successfully added as the root node."    #     ... update the response to reflect insertion. 
            self.numberOfElements += 1                                                #     ... update the numberOfElements by +1 
        else:                                                                         # Otherwise (if there already is a root node)...
            response = self.root.insertElement(pElement)                              #     ... update response to reflect the instance's return value of root.insertElement(pElement) and...
            self.numberOfElements += 1                                                #     ... update numberOfElements by +1
        return response                                                               # Return the response. 
      
      

    def search(self, pElement):
        response = False
        if self.root is None:                                                         # If there is no root
            print("The element was not found, as there are no values present.")       # Print the response
        else:                                                                         # If there is a root
            response = self.root.searchElement(pElement)                              # Response depends on parameter entering node
        return response                                                               #

      
      
##################################################################            Node Class           #################################################################################################
class Node:
    
    def __init__(self, pElement):                                               # Constructor function for Nodes; accepts input value of pElement 
        self.element = pElement                                                 # Assign the node's element as the input value 
        self.right = None                                                       # Nothing to the right  
        self.left = None                                                        # Nothing to the left 
        
        

    def insertElement(self, pElement):                                          # Declare an insertion function; self reference variable & pElement input value 
        answer = False                                                          # Declare and initialize answer as False 
        if pElement > self.element:                                             # If the input value is larger than node's value...
            if self.right is None:                                              #     ... AND, if there isn't already a right subtree (base function), then....
                self.right = Node(pElement)                                     #           ... create pElement as an instance of a node and assign it as the right value...
                answer = str(pElement) + " was successfully added."             #           ... and update answer to reflect addition.
            else:                                                               #     ... BUT, there is already a right subtree, ... 
                answer = self.right.insertElement(pElement)                     #           ... (recursion) repeat until there isn't a rightmost subtree.
        elif  pElement < self.element:                                          # OTHERWISE, if the input value is smaller than the node value...
            if self.left is None:                                               #     ... AND, if there isn't already a left subtree (base function), then....
                self.left = Node(pElement)                                      #           ... create pElement as an instance of a node and assign it as the left value...
                answer = str(pElement) + " was successfully added."             #           ... and update answer to reflect addition.
            else:                                                               #     ... BUT, there is already a left subtree, ... 
                answer = self.left.insertElement(pElement)                      #           ... (recursion) repeat until there isn't a leftmost subtree.
        return answer                                                           # Return the answer. 

      
      
    def searchElement(self, pElement):                                          # Declare a search function; self reference variable & pElement input value 
        response = str(pElement) + " does not exist in the tree."               # Initialize the response to indicate the object is not found.
        if pElement == self.element:                                            # (Base function) If the input value is equivalent to the element currently being compared...
            response = str(pElement) + " exists in the tree."                   #     ... Update response to reflect that the input value is contained in the tree. 
                                                                                
        elif pElement > self.element:                                           # OTHERWISE, if the input value is greater than the current element...
            if self.right is None:                                              #     ... (Base function) AND, if there is not a right subtree, then...
                response = str(pElement) + " does not exist in the tree."       #           ... Update the response to reflect that the input value is not contained in the tree.
            else:                                                               #     ... OTHERWISE (if there is a right subtree), then... 
                response = self.right.searchElement(pElement)                   #           ... Apply recursion until response updates or the tree has been searched and input is not found.

        elif pElement < self.element:                                           # OTHERWISE, if the input value is less than the current element...
            if self.left is None:                                               #     ... (Base function) AND, if there is not a left subtree, then...
                response = str(pElement) + " does not exist in the tree."       #           ... Update the response to reflect that the input value is not contained in the tree.
            else:                                                               #     ... OTHERWISE (if there is a left subtree), then... 
                response = self.left.searchElement(pElement)                    #           ... Apply recursion until response updates or the tree has been searched and input is not found.
                
        return response                                                         # Return the response. 

      
      
##################################################################            Functions Calls           #################################################################################################

myTree = Tree()
print("There are " + str(myTree.numberOfElements) + " elements in the tree.")
print(myTree.insert(99))
print(myTree.insert(42))
print(myTree.insert(31))
print(myTree.insert(6))
print(myTree.insert(14))
print(myTree.search(1000))
print(myTree.search(99))
print("There are " + str(myTree.numberOfElements) + " elements in the tree.")

