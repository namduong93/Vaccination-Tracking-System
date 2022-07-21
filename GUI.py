from re import T
from tkinter import *  
from DataHandler import *

import tkinter.messagebox as messagebox
import OCR

def showStatus():

    '''
    Display a dialogue box that shows the vaccination status of the person.
    '''
    
    stid = stuidVar.get()
    # 这里需要修改成对应函数
    res = getStatus(stid)
    if res == 1:
        messagebox.showinfo(message="This Student has been vaccinated")
    else:
        messagebox.showinfo(message="No vaccinated / No record")

noticeFlag = True
def useOCR():

    '''
    
    '''
    
    global noticeFlag
    if noticeFlag:
        messagebox.showinfo(message="Push c to detect Student ID. Push q to exit")
        noticeFlag = False
    res = OCR.ocrStudentID()
    stuidVar.set(res)

def chgStatus():

    '''
    Display a dialogue box that shows the success of changing vaccination status.
    Provides a function for radiobutton 
    '''
    
    status = changeType.get()
    status = 1 if status else 0
    changedid = changeId.get()
    changeStatus(changedid, status)
    messagebox.showinfo(message="Successful")

def login():
    
    '''
    Display a dialogue box through a if-else statement.
    '''
    
    adid = adminId.get()
    adpasswd = adminPasswd.get()
    if isAdmin(adid, adpasswd):
        adminLoginTk.destroy()
        changeStatusWindow()
    else:
        messagebox.showinfo(message="Id or Password is incorrect")
 
def changeStatusWindow():

    '''
    Display a layout for "Vaccination Status" including two Labels, one Entry, one Button, and one Radiobutton as Widget.
    Links to "useOCR" function if "OCR" button is clicked.
    Links to "showStatus" function if "Search" button is clicked.
    Links to "adminLoginWindow" function if "Admin" button is clicked.
    Links to "analysisWindow" function if "Analysis" button is clicked.
    '''
    global changeType
    global changeId

    top = Tk()  
    top.focus_force()
    changeType = BooleanVar(top)
    changeType.set(False)

    changeId = StringVar(top)
    top.geometry("330x200")  
    Stu_Id = Label(top, text = "ID Number: ").place(x = 20,y = 50)
    Status = Label(top, text = "Status:").place(x = 20,y = 90)
    e1 = Entry(top, textvariable=changeId).place(x = 100, y = 50)

    Check_T = Radiobutton(top, text="True",activebackground = "white", activeforeground = "blue", variable=changeType, value=True).place(x = 100, y = 90)
    Check_F =  Radiobutton(top, text="False",activebackground = "white", activeforeground = "blue", variable=changeType, value=False).place(x = 170, y = 90)

    Save = Button(top, text = "Save",activebackground = "white", activeforeground = "blue", command=chgStatus).place(x = 140, y = 140)

    top.title('Vaccination Status')
    top.mainloop()

def analysisWindow():

    '''
    Provides a layout for "Data Analysis", and two Labels and one Button.
    Close the "Data Analysis" window after "OK" button is clicked.
    '''
    global analysisTk
    analysisTk = Tk()

    analysis = getAnalysis()
    analysisTk.geometry("300x250")  
    Percentage = Label(analysisTk, text = f"Percentage = {analysis[0]}%").place(x = 6,y = 50)  
    TotNum = Label(analysisTk, text = f"Total Number = {analysis[1]}").place(x = 10, y = 90)   
    analysisTk.title("Data Analysis")
    exit_button = Button(analysisTk, text="OK", activebackground= "white", activeforeground = "blue", command=analysisTk.destroy).place(x = 130, y = 145)
    analysisTk.mainloop()


def adminLoginWindow():

    '''
    Provides a layout for "Administrator Login" and two Entries for user input. 
    Llnks to the function "Login" after clicking "Search" button.   
    '''
    
    global adminId
    global adminPasswd
    global adminLoginTk

    adminLoginTk = Tk()  
    adminLoginTk.focus_force()
    adminId = StringVar(adminLoginTk)
    adminPasswd = StringVar(adminLoginTk)

    adminLoginTk.geometry("300x250")  
    Adm_Id = Label(adminLoginTk, text = "ID Number: ").place(x = 10,y = 50)  
    password = Label(adminLoginTk, text = "Password: ").place(x = 10, y = 90)  
    e1 = Entry(adminLoginTk, textvariable=adminId).place(x = 80, y = 50)  
    e2 = Entry(adminLoginTk, show="*", textvariable=adminPasswd).place(x = 80, y = 90)  
    search = Button(adminLoginTk, text = "Login",activebackground = "white", activeforeground = "blue", command=login).place(x = 130, y = 145)  
    adminLoginTk.title('Administrator Login')
    adminLoginTk.mainloop()

def queryWindow():

    '''
    Display a layout for "Vaccination Status" including four Buttons, one Entry, and one Label as Widget.
    Links to "useOCR" function if "OCR" button is clicked.
    Links to "showStatus" function if "Search" button is clicked.
    Links to "adminLoginWindow" function if "Admin" button is clicked.
    Links to "analysisWindow" function if "Analysis" button is clicked.
    '''
    global stuidVar
    
    top = Tk()
    top.focus_force()
    stuidVar = StringVar()
    top.geometry("330x200")  
    Stu_Id = Label(top, text = "Student ID: ").place(x = 20,y = 50)  
    OCR_s = Button(top, text = "OCR",activebackground = "white", activeforeground = "blue", command=useOCR).place(x = 110, y = 90) 
    Search = Button(top, text = "Search",activebackground = "white", activeforeground = "blue", command=showStatus).place(x = 160, y = 90)  
    Additional = Button(top, text = "Admin",activebackground = "white", activeforeground = "blue", command=adminLoginWindow).place(x = 280, y = 0)
    Analysis = Button(top, text = "Analysis",activebackground = "white", activeforeground = "blue", command=analysisWindow).place(x = 0, y = 0)
    studentInput = Entry(top, textvariable=stuidVar).place(x = 100, y = 50)   
    top.title('Vaccination Status')
    top.mainloop()

def GUI():
    queryWindow()
