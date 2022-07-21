from OCR import *
from DataHandler import *
from GUI import *

def typeQuery():
    """
    Get the users' studentID
    Return 1 to show that the users has been vaccinated
    Else, the user has not been vaccinated or has no record
    """

    stid = input("Please enter studentID here: ")
    res = getStatus(stid)
    if res == 1:
        print("This student has been vaccinated.")
    else:
        print("No vaccinated / No record")


def OCRQuery():
    """
    Get studentID by using OCR mode
    Let the user judge whether the analysis is correct or not
        If the displayed result is correct then perdorrm a query on the studentID
        Else it will be reacquired
    Return 1 to show that the users has been vaccinated
    Else, the user has not been vaccinated or has no record
    """
    stid = ""
    while True:
        stid = ocrStudentID()
        res = input(f"Is this id correct, {stid}? Yes/No")
        if res == "Yes":
            break
    res = getStatus(stid)
    if res == 1:
            print("This student has been vaccinated.")
    else:
        print("No vaccinated / No record")

def queryCMD():
    """
    Allow users to enter their studentID by entering a number to select a perferred mode to enter their studentID
    If there is a fault,users can enter -1 to exit this application completely
    """
    while True:
        print("Please enter the mode that you need. Enter 1 if you prefer manual input. If you are more fond of mode OCR, you can enter 2. You can also enter 3 to choose display analysis mode. And if you want sigu out this app, you can enter -1 :")
        scheme = int(input("Please enter a number to select the mode you want: "))
        if scheme == 1:
            typeQuery()
        elif scheme == 2:
            OCRQuery()
        elif scheme == 3:
            ans = getAnalysis()
            print(f"Vaced Percentage: {ans[0]}. Vaced Numer: {ans[1]}")
        elif scheme == -1:
            return

def adminCMD():
    """
    Ask the users to enter their ID and their password
    Use function to determine if they have entered it correctly
        If correct, the users can enter their studentID and update their vaccination status
        Else, they need to enter again
    If there is a fault,users can enter -1 to exit this application completely
    """
    while True:        
        id = input("Please enter your studentId or enter -1 if you want to sign out this app :")
        if id == "-1":
            return
        passwd = input("Please enter your password:")
        isAd = isAdmin(id, passwd)
        if isAd:
            break
    while True:
        studentId = input("Please enter studentId to change or enter -1 if you want to exit this status: ")
        if studentId == "-1":
            return
        status = int(input("Please enter your currect status, 0 if you have not been vaccinated, 1 if you have been vaccinated: "))
        status = 1 if status else 0
        changeStatus(studentId,status)
        if status == -1:
            return


def CMD():
    """
    Allow users to enter their studentID by entering a number to select a perferred mode 
    If there is a fault,users can enter -1 to exit this application completely
    """
    print("Please select the function you prefer.Enter 1 if you prefer query mode.If you are more fond of administration mode, please enter 2. And you can enter 3 for choosing GUI mode. ")
    scheme = int(input("Please enter the number to select the mode you want: "))
    if  scheme == 1:
        #scheme1-use OCR
        queryCMD()
    elif scheme == 2:
        #scheme2-enter studentId directly
        # studentId = input("please enter your studentId:")
        adminCMD()
    elif scheme == 3:
        GUI()