from DataHandler import *
from DataTransfer import *
from OCR import *
from GUI import *
from CMD import *

import sys

def initial():
    """
initial the program, download the data
    """
    getData('data.data')
    getData('auth.data')
    loadData()
    print("[Main]: Load data Successfully")

def end():
    """
the end of the program. if admin make change, the new version will be upload.
    """
    if getChangeFlag():
        storeData()
        uploadData('data.data', 'data')
        uploadData('auth.data', 'auth')
        print("[Main]: Upload file successfully")
    print("[Main]: System shutdown")

def addAdmin():
    """
add an admin to the system
    """
    initial()
    acc = input("Please input a current Administrator Account: ")
    passwd = input("Please input corresponding Password: ")
    if isAdmin(acc, passwd):
        acc = input("Please input new Administrator Account: ")
        passwd = input("Please input corresponding new Password: ")
        addAccountForAdmin(acc, passwd)
        end()
    else:
        print("Auth failure! Please try again")

def gui_main():
    initial()
    GUI()
    end()

def cl_main():
    initial()
    CMD()
    end()

if len(sys.argv) > 0:
    if "-h" in sys.argv or "--help" in sys.argv:
        print("""
PolyU Vaccine
    -g, --GUI [default enable]
        GUI mode
    -c, --command
        Command line mode
    -h, --help
        Show this help message
    --add-admin
        Add another admin
        """)
    elif "--add-admin" in sys.argv:
        addAdmin()
    elif "-g" in sys.argv or "--GUI" in sys.argv:
        gui_main()
    elif "-c" in sys.argv or "--command" in sys.argv:
        cl_main()
    else:
        gui_main()
