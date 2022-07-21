import random
import string

Data={}
Data2={}
ChangeFlag = False

def getChangeFlag():
    return ChangeFlag

def loadData():
    """
    The first part of this function will read the file called data.data, and split it into 2 part:
        1. Student Id
        2. Status (0/1) (0/1 is represented for non-vaccinated and vaccinated)
    The Data will be stored into the dictionary called Data. 
    While the key is the Student Id, the Status is the value.

    The second part of this fuction will read the file called auth.data, and split it into 3 part.
        1. Admin's Account
        2. Key
        3. Hash Code
    The Data will be store into the dictionary called Data2.
    While the key of Data2 is Account, the value will be a tuple, which are Key and and Hash Code, respectively
    """
    f=open("data.data","r")
    f.readline()
    for line in f.readlines():
        stdID,stt = line.split(";")
        stt=int(stt[0:1])
        Data[stdID]=stt
    f.close()
    f=open("auth.data","r")
    f.readline()
    for line in f.readlines():
        rAcc,rKey,rPass = line.split(";")
        Data2[rAcc]=(rKey,rPass)
    f.close()

def getStatus(StudentID):
    """
    This function will get the Vaccine information of Student/Staff

    Input: 
        Student ID: the ID of Student/staff 
    Output:
        0: Student/staff is not vaccinated
        1: Student/staff is vaccinated 
        -1: Unknown
    """
    if StudentID in Data:
        return Data[StudentID]
    else:
        return -1

def changeStatus(StudentID, status):
    """
    This function allows admin to change Student's status from the Data.

    Input:
        Student ID: the ID of Student/staff 
        status: 0/1
    """
    global ChangeFlag
    ChangeFlag = True
    if StudentID in Data:
        Data[StudentID]=status
    else:
        Data[StudentID]=status
    print(f"[DataHandler]: changeStatus({StudentID}, ***)")

def storeData():
    """
    This function will write the data from the Data into the data.data file:
    The form should be:
        Student ID;Status
        123;1
        21107569;1
    """
    f=open("data.data","w")
    f.write("Student ID;Status\n")
    for key in Data:
        f.write(key)
        f.write(";")
        f.write(chr(Data[key]+ord("0")))
        f.write("\n")
    f.close()

#Hasing
def Encrypt(SuperStrongAndUnbreakableAccount):
    """
    This is a function to encrypt the account based on MD5 algorithm.
    Input:
        SuperStrongAndUnbreakableAccount: the string from addAccountForAdmin() fuction
    Output:
        A number
    """
    HashT=0
    base=93
    MOD=1000000093
    for i in SuperStrongAndUnbreakableAccount:
        HashT=(HashT*base+ord(i)-ord('0'))%MOD
    return str(HashT)

#Store Admin data 
def addAccountForAdmin(acc,passwd):
    """
    This function will allow Admin to add new Addmin's account and write it into the auth.data file.
    Here is the details:
        1. random a string for each account
        2. add the key before the account
        3. encrypt it 
        4. write to the auth.data file

    Input: 
        acc: new admin account
        passwd: new admin password
    """
    global ChangeFlag
    ChangeFlag = True
    f=open("auth.data","a")
    key="".join(random.choices(string.ascii_lowercase,k=10))
    f.write(acc)
    f.write(";")
    f.write(key)
    f.write(";")
    f.write(Encrypt(key+passwd))
    f.write('\n')
    f.close()
    loadData()

#Check if Admin or not
def isAdmin(acc,passwd):
    """
    After recieving the account and password, this function will encrypt the Password based on the Key.
    The Password will then be checked if it is match with the real Password or not.
    """
    if acc in Data2:
        if Encrypt(Data2[acc][0]+passwd)+"\n" == Data2[acc][1]:
            return True
        else:
            return False
    else:
        return False

def getAnalysis():
    """
    This function will take the Vaccination Information Analysis based on the Data file.

    Output:
        The percentage of vaccinated students/staff and the number of vaccinated students/staff.
    """
    loadData()
    cnt=0
    cnt1=0
    for key in Data:
        if Data[key]==True:
            cnt1+=1
        cnt+=1
    return round(cnt1/cnt*100,2), cnt1