'''
Created on Oct 19, 2017

@author: Jocelyn Chen
'''
# import module
import sys

################  Global Variables  ##################
# TODO: 
def Grocery_List():
# Declare a Grocery_List variable which should keep all the grocery information
# The Grocery_List should contain item, and its price 
    Grocery_List = []   #[item_name, item_price, item_number]
# boolean to maintain the for loop for the main
run = True

# Helper functions
######## Input for Int or Float ################
def cast_int(arg):
    try:
        return int(arg)
    except ValueError:
        print("Please make sure you enter an integer")
        return ValueError
    
def cast_float(arg):
    try:
        return float(arg)
    except ValueError:
        print("Please make sure you enter an float")
        return ValueError

# Get user input and check if it is a Integer or Floating number
# Prompt: the prompt to ask user for input
# Type: the type of what input type should be, can be either "Integer" or "Float"
def make_sure_type_input(prompt, type):
    type_map = {
        'Integer': cast_int,
        'Float': cast_float
    }
    while(True):
        user_input = input(prompt)
        res = type_map[type](user_input)
        if(res != ValueError): 
            return res

############################################

# Print Grocery List
def printList():
    print("Current Grocery List:")
    for item in Grocery_List():
        print(item[0] + "\t" + item[1] + "\t" + item[2] + "\t" + item[3])
    # TODO: Print all item in Grocery List here

# Insert an Item to the Grocery List
def insertItem():
    print("Insert an item to the grocery list: ")
    item_name = input("Enter item name: ")
    item_price = input("Enter item price: ")
    item_number = input("Enter item number: ")
    Grocery_List.append([item_name, item_price, item_number])
    # TODO: ask user to insert item name, price, and quantity, and add the results to the grocery list
    # HINT 1: make use of the make_sure_type_input() function when ask user to enter a number
    # HINT 2: you should insert into the grocery list using the function append()
    
# Delete Grocery List
def deleteItem():
    print("Delete an item from the grocery list")
    item_name = input("Enter the exact item name you want to delete: ")
    for i in range(len(Grocery_List)):
        item = Grocery_List[i]
        if(item[0] == item_name):
            Grocery_List.pop(i)
            break;
    print("The item name you entered is not in the list!")
    
# Clear Grocery List
def clearItem():
    print("Clear list")

    Grocery_List = []
    # TODO: Implement the function that empty the grocery list
    
# Calculate the output
def calculate():
    print("Calculate the total cost for your shopping plan...")

    total_price = 0
    for item in Grocery_List:
        total_price = total_price + item[1]*item[2]
        print("Total price is: ", + total_price)
    # TODO: Calculate the total price

    print("Happy Shopping! :)")

def processInput(option):
    if (option == 1):
        printList()
    elif (option == 2):
        insertItem()
    elif (option == 3):
        deleteItem()
    elif (option == 4):
        clearItem()
    elif (option == 5):
        calculate()
    elif (option == 6):
        # This is the quit option, we quit the program
        print("Quitting the program...")
        sys.exit(0)

# Get user input
def getInput():
    return make_sure_type_input("Choose from 1 to 6: ", "Integer")

# Show menu to users
def showMenu():
    print("Choose from the following options:")
    print("1. Show the current grocery list")
    print("2. Add a new item to the list")
    print("3. Remove an item from the list")
    print("4. Clear the list")
    print("5. Calculate the shopping list")
    print("6. Quit")

if __name__ == '__main__':
    # Main Menu
    print("Welcome to the spending calculator!")
    while(run):
        showMenu()
        processInput(getInput())
