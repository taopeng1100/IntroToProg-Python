# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# Tao Peng, 06.04.2021, Started script
# <Tao Peng>,<05.04.2021>,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants

File = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open(File, "r")
for row in objFile:
    lstRow = row.split(",")
    dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Here are the current data:", "\n")
        for objRow in lstTable:
            print(objRow)
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strID = str(input("Enter a task: "))
        strName = str(input("Enter priority: "))
        dicRow = {"Task": strID, "Priority": strName}
        lstTable.append(dicRow)
        print("Here is the current data in lstTable:")
        for objRow in lstTable:
            print(objRow)
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        task_to_rv = str(input("Enter the name of a task you like to remove: "))
        for dicRow in lstTable:
            if(dicRow["Task"] == task_to_rv):
                lstTable.remove(dicRow)
            else:
                print("dicRow NOT found")
        print("The task of", task_to_rv, "removed")
        print("The current lstTable is: ", "\n", lstTable)
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(File, "w")
        for dicRow in lstTable:
            objFile.write(str(dicRow["Task"]) + "," + str(dicRow["Priority"]) + "\n")
        objFile.close()
        print("The current data are saved in ToDOList.txt")
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        break  # and Exit the program
