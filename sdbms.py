import os
import getpass
import time

def inputTeacher():
    ID=input("Enter the id of the teacher            : ")
    if idexistence(ID,'teacherinfo.txt'):
        print("ID already exists.Try Again.")
        return []
    name=input("Enter the name of the teacher          : ")
    grade=input("Enter the class taught by the teacher  : ")
    subject=input("Enter the subject taught by the teacher: ")
    li=[ID,name,grade,subject]
    li2=[ID,name,'password','N']
    ST_login(li2,'teacherlogin.txt')
    return li

def inputStudent():
    ID=input("Enter the id of the Student            : ")
    if idexistence(ID,'studentinfo.txt'):
        print("ID already exists.Try Again.")
        return []
    name=input("Enter the name of the Student          : ")
    grade=input("Enter the class of the Student         : ")
    marks=input("Enter the marks obtained in Maths, Physics,CS, English and Chemistry, separated by space : ").split()
    
    li=[ID  ,name,grade,*marks]
    li2=[ID,name,'password','N']
    ST_login(li2,'studentlogin.txt')
    return li
def idexistence(ID,filename):
    file=open(filename,'r')
    li=file.readlines()
    file.close()
    flag=0
    for l in li[2::]:
        if l.split()[0]==ID:
            return True
        else:
            flag=0
    if flag==0:
        return False
    
def search(ID,filename):
    flag=0
    file=open(filename,'r')
    if filename=='studentinfo.txt':
        u_name='student'
        header="ID\tName \tClass\tMaths\tPhysics\tCS\tEnglish\tChemistry"
    elif filename=='teacherinfo.txt':
        u_name='Teacher'
        header="ID\tName \tGrade\tSubject"
    else:
        u_name=''
        header='\n'
    for data in file.readlines():
        for ids in data.split():
            if ids==ID:
                print(f"\nThe required {u_name} details are: ")
                print(header)
                print(data)
                flag=1
                break
    if flag==0:
        print(f"\n{u_name}'s Detail not found")       
    file.close()



def new_add(filename):
    file=open(filename,'a')
    if filename=='studentinfo.txt':
        li=inputStudent()
        user='student'
    else:
        user='teacher'
        li=inputTeacher()
    if len(li)==0:
        return
    
    for i in li:
        file.write(i)
        file.write("\t")
    file.write("\n")
    file.close()
    print(f"\nThe {user} has been added successfully\n")

def datacolumnteacher():   
    file=open("teacherinfo.txt",'w+')
    file.write("ID\tName\tClass\tSubject\n")
    file.write("\n")
    file.close()
def datacolumnstudent():
    file=open("studentinfo.txt",'w+')
    file.write("ID\tName\tClass\tMaths\tPhysics\tCS\tEnglish\tChemistry\n")
    file.write("\n")
    file.close()
def ST_login(li2,filename):
    file=open(filename,'a')

    filesize=os.path.getsize(filename)
    if filesize==0:
        file.write('\n\n')
        for data in li2:
            file.write(data)
            file.write("\t")
    else:   
        for data in li2:
            file.write(data)
            file.write("\t")
    file.write("\n")
    file.close()


def updatestudent():
    li=[]
    try:
        file=open("studentinfo.txt",'r+')
        for data in file.readlines():
            li.append(data)
        file.close()
    except IOError:
        print("There is no data available")
        return
    ID=input("Enter the ID of the student whose data you want to update: ")
    rowno=2
    flag=0
    for row in li[2::]:
        if row.split()[0]==ID:
            update=input("Enter updated marks separated by space: ").split()
            name=li[rowno].split()[1]
            grade=li[rowno].split()[2]
            li[rowno]=ID+'\t'+name+'\t'+grade
            for j in update:
                li[rowno]+='\t'+j
            li[rowno]+='\n'
            flag=1
            print("Student Data has been successfully Updated.")
            break
        else:
            rowno+=1
    file=open("studentinfo.txt",'w+')
    for i in li:
        file.write(i)
    file.close()      
    if flag==0:
        print("Student info not found with the entered ID")

def updateteacher():
    li=[]
    try:
        file=open("teacherinfo.txt",'r+')
        for data in file.readlines():
            li.append(data)
        file.close()
    except IOError:
        print("There is no data available")
        return
    ID=input("Enter the ID of the teacher whose data you want to update: ")
    rowno=2
    flag=0
    for row in li[2::]:
        if row.split()[0]==ID:
            grade=input("Enter the class taught by the teacher  :  ")
            sub=input("Enter the subject taught by the teacher: ")
            name=li[rowno].split()[1]
            li[rowno]=ID+'\t'+name+'\t'+grade+'\t'+sub+'\n'
            flag=1
            print("Teacher Data has been successfully Updated.")
            break
        else:
            rowno+=1
    file=open("teacherinfo.txt",'w+')
    for i in li:
        file.write(i)
    file.close()
    if flag==0:
        print("Teacher info not found with this ID")

def removedata(filename,ID):
    li=[]
    remove=''
    try:
        file=open(filename,'r+')
        for data in file.readlines():
            li.append(data)
        file.truncate()
        file.close()
    except IOError:
        print("There is no data available")
        return
    rowno=2
    flag=0
    for row in li[2::]:
        if row.split()[0]==ID:
            remove=li.pop(rowno)
            flag=1
            print("The data has been successfully removed.")
            break
        else:
            rowno+=1
    file=open(filename,'w+')
    for i in li:
        file.write(i)
    file.close()
    file2=open('archive.txt','a')
    file2.write("Data removed on: ")
    file2.write(time.asctime())
    file2.write(remove)
    file2.write("\n")
    file2.close()
    if filename=='studentinfo.txt':
        removedata('studentlogin.txt',ID)
    elif filename=='teacherinfo.txt':
        removedata('teacherlogin.txt',ID)
    if flag==0:
        print("No information found with the entered ID")
def updatelogin(ID,name,passenter,filename):
    li=[]
    try:
        file=open(filename,'r+')
        for data in file.readlines():
            li.append(data)
        file.truncate()
        file.close()
    except IOError:
        print("There is no data available")
        return
    rowno=2
    flag=0
    if passvalidity(passenter):
        pass
    else:
        return
    cnf_pass=input("Confirm your new password: ")
    if cnf_pass==passenter:
        pass
    else:
        print("Password didn't match.Login again and try.")
        return
    for row in li[2::]:
        if row.split()[0]==ID:
            li[rowno]=ID+'\t'+name+'\t'+passenter+'\t'+'Y'+'\t'+time.asctime()+'\n'
            flag=1
            print("You have successfully changed your password.Login again using your ID to continue")
            break
        else:
            rowno+=1
    file=open(filename,'w+')
    for i in li:
        file.write(i)
    file.close()
    if flag==0:
        print("No data found with the entered ID")
    

def passvalidity(passenter):
    countA=counta=count1=countschar=0
    l=len(passenter)
    schar=['@','&','!','#','$','%']
    for i in passenter:
        if 'A'<=i<='Z':
            countA+=1
        elif 'a'<=i<='z':
            counta+=1
        elif '0'<=i<='9':
            count1+=1
        elif i in schar:
            countschar+=1
    if countA>0 and counta>0 and count1>0 and countschar>0 and l>5:
        return True
    else:
        print("Password requirement not fulfilled.\nThe new password should be of atleast 6 charachers.")
        print("It must contain atleast a small alphabet,a capital alphabet ,a number and a special character (@&!#$%)")
        return False

def adminlogincredential():
    username='admin'
    password='admin'
    p1=getpass.getpass("Enter Password: ",None)
    if p1==password:
        adminfun(username)
    else:
        print("Invalid Password.Try again after some time")

def logincredential(ID,filename):
    file=open(filename,'r+')
    li=[]
    check=0
    
    for data in file.readlines():
            li.append(data)
    file.close()
    try:
        for row in li[2::]:
            if row.split()[0]==ID:
                name=row.split()[1]
                pass1=row.split()[2]
                flag=row.split()[3]
                check=1
                break
            else:
                check==0
    except IndexError:
        print("")
    if check==0:
        print("Invalid ID. Please enter correct ID or contact admin")
        m=int(input("Press 1 to send a message to the admin: "))
        if m==1:
            messageadmin()
        return
    if flag=='N':
        print(f"Hey {name}, this is your first login.Lets secure your data by resetting your password") 
        passenter=input("Enter New Password: ")
        if passvalidity(passenter):
            updatelogin(ID,name,passenter,filename)
        else:
            print("Try Again")
    else:
        pass2=getpass.getpass("Enter Password: ")
        if pass2==pass1:
            if filename=='studentlogin.txt':
                studentfun(ID,name)
            else:
                teacherfun(ID,name)
        else:
            print("Incorrect Password.Please login after some time")

def messageadmin():
    file2=open("adminmessages.txt",'a')
    file2.close()
    filesize=os.path.getsize("adminmessages.txt")
    if filesize==0:
        file1=open("adminmessages.txt",'w+')
        new='NO\n0\n0\n'
        file1.write(new)
        file1.close()        
    file=open("adminmessages.txt",'a+')
    name=input("Name: ")
    ids=input("ID  : ")
    msg=input("Your Message: ")
    compmsg=time.asctime()+"\tFrom: "+name+"\t ID: "+ids+"\t Message: "+msg+'\n'
    file.write(compmsg)
    print(f"Dear {name},\nYour message has been successfully sent to the admin.")
    file.close()
    file=open("adminmessages.txt",'r')
    li=[]
    read=0
    for data in file.readlines():
        li.append(data)
        read+=1
    file.close()
    unread=int(li[1])
    unread+=1
    li[1]=str(unread)+'\n'
    updateadminmessage('YES',unread,read-unread)
def updateadminmessage(new,unread,read):
    file=open("adminmessages.txt",'r')
    li=[]
    for data in file.readlines():
        li.append(data)
    file.close()
    li[0]=new+'\n'
    li[1]=str(unread)+'\n'
    li[2]=str(read)+'\n'
    file=open("adminmessages.txt","w+")
    for line in li:
        file.write(line)
    file.close()
def readmessages():
    print("Your Messages are: \n")
    file=open("adminmessages.txt",'r')
    for line in file.readlines()[:2:-1]:
        print(line)
    unread=0
    read=0
    updateadminmessage('NO',unread,read)
    file.close()



def adminfun(username):
    print("=======================================================================================================================================================")    
    print(f"\tWelcome {username}")
    li=[]
    try:
        file=open("adminmessages.txt",'r')
        li=file.readlines()
        file.close()
        if li[0]=='YES\n':
            unread=li[1]
            m1=int(input(f"Dear {username},\nYou have {unread.strip()} new message(s).Press 1 to open inbox, 0 to skip. "))
            if m1==1:
                readmessages()
    except IOError:
        print("")
    
    print("Choose the operation You want to do:")
    print("1.Add a Student\n2.Add a Teacher\n3.Search a Student\n4.Search a Teacher\n5.Update Student Data\n6.Update Teacher Data")
    print("7.Remove Student\n8.Remove Teacher\n9.Open Inbox\n10.Log Out\n")
    choice=int(input("Enter your choice: "))
    while(choice):
        if choice==1:
            file=open("studentinfo.txt",'a')
            file.close()
            filesize=os.path.getsize("studentinfo.txt")
            if filesize==0:
                datacolumnstudent()
                new_add("studentinfo.txt")
            else:
                new_add("studentinfo.txt")

        elif choice==2:
            file=open("teacherinfo.txt",'a')
            file.close()
            filesize=os.path.getsize("teacherinfo.txt")
            if filesize==0:
                datacolumnteacher()
                new_add("teacherinfo.txt")
            else:
                new_add("teacherinfo.txt")

            
        elif choice==3:
            try:
                file=open("studentinfo.txt")
                file.close()
                ID=input("Enter the ID of the Student: ")
                search(ID,'studentinfo.txt')
            except IOError:
                print("There is no data available currently.Kindly add some data first")
            

        elif choice==4:
            try:
                file=open("teacherinfo.txt")
                file.close()
                ID=input("Enter the ID of the Teacher: ")
                search(ID,'teacherinfo.txt')
            except IOError:
                print("There is no data available currently.Kindly add some data first")
        elif choice==5:
            updatestudent()
        elif choice==6:
            updateteacher()
        elif choice==7:
            ID=input("Enter the ID whose data you want to remove: ")
            removedata("studentinfo.txt",ID)
        elif choice==8:
            ID=input("Enter the ID whose data you want to remove: ")
            removedata("teacherinfo.txt",ID)
        elif choice==9:
            try:
                readmessages()
            except IOError:
                print("Inbox is empty")
        elif choice==10:
            print("You have been successfully logged out.Thank You!")
            return
        else:
            print("Invalid Input")
        print("\nChoose the operation You want to do:")
        print("1.Add a Student\n2.Add a Teacher\n3.Search a Student\n4.Search a Teacher\n5.Update Student Data\n6.Update Teacher Data")
        print("7.Remove Student\n8.Remove Teacher\n9.Open Inbox\n10.Log Out\n")
        choice=int(input("Enter your choice: "))
def studentfun(ID,name):
    print(f"\nWelcome Dear {name} \n")
    print("Choose the operation You want to do:")
    print("1.View your details\n2.Change your password\n3.Contact Admin\n4.Log Out")
    choice=int(input("Enter your choice: "))
    while(choice):
        if choice==1:
            try:
                file=open("studentinfo.txt")
                file.close()
                search(ID,"studentinfo.txt")
            except IOError:
                print("There is no data available currently.Kindly contact admin.")
            
        elif choice==2:
            passenter=input("Enter the new password: ")
            updatelogin(ID,name,passenter,"studentlogin.txt")
            return
        elif choice==3:
            messageadmin()
        elif choice==4:
            print("You have been successfully logged out.")
            print("Thank You for using the Student Managment System!")
            return
        else:
            print("Invalid Input")
        print(f"\nWelcome Dear {name}\n")
        print("Choose the operation You want to do:")
        print("1.View your details\n2.Change your password\n4.Contact Admin\n5.Log Out")
        choice=int(input("Enter your choice: "))
def teacherfun(ID,name):
    print(f"\nWelcome Dear {name} \n")
    print("Choose the operation You want to do:")
    print("1.Search a Student\n2.Search a Teacher\n3.Update Student Marks\n4.Change your password\n5.Contact Admin\n6.Log Out")
    choice=int(input("Enter your choice: "))
    while(choice):
        if choice==1:
            try:
                file=open("studentinfo.txt")
                file.close()
                ID=input("Enter the ID of the Student: ")
                search(ID,"studentinfo.txt")
            except IOError:
                print("There is no data available currently.Kindly contact admin.")
            
        elif choice==2:
            try:
                file=open("teacherinfo.txt")
                file.close()
                ID=input("Enter the ID of the Teacher: ")
                search(ID,"teacherinfo.txt")
            except IOError:
                print("There is no data available currently.Kindly contact admin.")
        elif choice==3:
            updatestudent()
        elif choice==4:
            passenter=input("Enter the new password : ")
            updatelogin(ID,name,passenter,"teacherlogin.txt")
            return
        elif choice==5:
            messageadmin()
        elif choice==6:
            print("You have been successfully logged out.")
            print("Thank You for using the Student Managment System!")
            return
        else:
            print("Invalid Input")
        print(f"\nWelcome Dear {name} \n")
        print("Choose the operation You want to do:")
        print("1.Search a Student\n2.Search a Teacher\n3.Update Student Marks\n4.Change your password\n5.Contact Admin\n6.Log Out")
        choice=int(input("Enter your choice: "))


def main():
    print("=======================================================================================================================================")
    choice=int(input("\t\tWelcome To The Student Database Manangement System!\nKindly select from the options to continue.I am, \n1.Admin\n2.Teacher\n3.Student\n4.Exit\n"))
    print("=======================================================================================================================================")

    while(choice):
        if choice==1:
            adminlogincredential()
        elif choice==2:
            ID=input("Enter your ID : ")
            try:
                logincredential(ID,"teacherlogin.txt")
            except IOError:
                print("Nothing to show. Kindly contact admin")
                m=int(input("Press 1 to send a message to the admin: "))
                if m==1:
                    messageadmin()
        elif choice==3:
            ID=input("Enter your ID : ")
            try:
                logincredential(ID,"studentlogin.txt")
            except IOError:
                print("Nothing to show. Kindly contact admin.")
                m=int(input("Press 1 to send a message to the admin: "))
                if m==1:
                    messageadmin()
        elif choice==4:
            print("=======================================================================================================================================")
            print("\t\t\tThank You for using the Student Database Managment System!")
            print("=======================================================================================================================================")

            break
        else:
            print("Invalid Input.Thank you. Try again after some time.")
            
        print("\n=======================================================================================================================================")
        choice=int(input("\n\n\t\tWelcome To The Student Database Manangement System!\nKindly select from the options to continue.I am, \n1.Admin\n2.Teacher\n3.Student\n4.Exit\n"))

def ReadMe():
    print("**********************************************************************************************************************************************")
    
    print("\nABOUT THE PROJECT")
    print("The project gives you three ways to log in and use the student management system.")
    print("These are as follows:")
    print("1. Admin	2.Teacher	3.Student")
    print("\nThe Admin has all the facilities like adding student and teacher,searching a particular student or teacher,\n removing student and teacher and updating the information of the teacher and student.")
    print("The Teacher has functionalities like searching a student or teacher, updating the information of the student \nand changing their respective password.")
    print("The Student can view his/her details and can reset his/her password.")
    print("The Student and teacher can send DMS to the admin.")
    print("Please Note: ")
    print("->The password of admin is admin")
    print("->The default password for students and teacher is password and they need to create a new password during their first login.")

    print("\n==================================")
    print("UNIQUE FEATURES OF THE PROJECT:")
    print("==================================\n")
    print("->No files needs to be created before the execution of the program.The files gets create automatically by the system as and when required.")
    print("  All the associated files gets created at the location of this .py file.")
    print("->All the possible exceptions handling has been done.")
    print("->The data are represented in tabular form thus it improves the readability.")
    print("->Utmost care has been taken to set and update the password of students and teachers securely.")
    print("->Separate files has been created that stores the login information of students and teachers so as to protect the information and thus decreasing the chances of misusing the login information.")
    print("  In case, a file gets hacked , the other details remain protected.")
    print("->The login information of the teacher and students are not accessible even by the admin via this code. So worry less, Your password is secured.")
    print("  The details like date and time of updating the password is recorded by the system so as to facilitate password change due to expiry in the future versions.")
    print("->Once the details of student or teacher is removed, it gets stored in another file named archive for future reference that might be helpful for the various categories of users.")
    print("  The time and date of deletion of data is recorded in the same file.")
    print("->The code has been kept as simple as possible and the reuse of functions is taken care of.")
    print("->The project has been done in a way keeping the practical usability and requirements in mind.")
    print("  Hence it can be used in the various fields for managing the data.")

    print("\nThank you for choosing my code. Kindly feel free to give suggestions on the scope of improvement of the project.")

    print("\nHope You get everything you expect from this code and that too without any hassle.\n\n")
    print("**********************************************************************************************************************************************")

print("\n=======================================================================================================================================\n")
x=int(input("Welcome.\nChoose from the options to continue.\n1.Start using the Application\n2.View ReadMe File and then use application\n"))
if x==1:
    main()
elif x==2:
    ReadMe()
    main()
else:
    print("Invalid Input.Exiting.")
