import os
import platform
import mysql.connector
import pandas as pd
mydb = mysql.connector.connect(host="localhost",user="user",passwd="####",port="2004",database="Database") ##Enter host, username, password, port and database details from SQL
mycursor=mydb.cursor()
def course_Insert():
    L=[]
    c_id=int(input("Enter the id: "))
    L.append(c_id)
    stream=input("Enter the Stream: ")
    L.append(stream)
    C_name=(input("Enter available opportunities in this stream :"))
    L.append(C_name)
    course=(L)
    sql="insert into course_details (c_id, stream, c_name) values (%s, %s, %s)"
    mycursor.execute(sql, database)
    mydb.commit()
def cView():
    print("Select the search criteria :")
    print("1. c_id")
    print("2. Stream")
    print("3. All")
    ch=int (input("Enter choice: "))
    if ch==1:
        s=int (input("c_id :"))
        c=(s,)
        sql="select * from course_details where c_id=%s"
        mycursor.execute(sql, c)
    elif ch==2:
        s=input("Enter stream: ")
        n=(s,)
        sql="select * from course_details where c_name=%s"
        mycursor.execute(sql,n)
    elif ch==3:
        sql="select * from course_details"
        mycursor.execute(sql)
    res = mycursor.fetchall()
    print("The course details are as follows:")
    print(" (course_id, Stream_Name, Course_opportunities)")
    for x in res:
        print(x)
def removecourse():
    cid=int(input("Enter the course_id of the course to be deleted :"))
    ci=(cid,)
    sql="Delete from course_details where c_id=%s"
    mycursor.execute(sql,ci)
    sql="Delete from course_details where c_id=%s"
    mycursor.execute(sql,ci)
    mydb.commit()
def MenuSet():
    print("Enter 1: To Add ")
    print("Enter 2: To View ")
    print("Enter 3: To Remove ")
    try:
        userInput = int(input("Please Select An Above Option:"))
    except ValueError:
        exit("\nThat's Not A Number")
    else:
        print("\n") 
        if(userInput == 1):
            course_Insert()
        elif (userInput ==2):
            cView()
        elif (userInput==3):
            removecourse()
        else:
            print("Enter correct choice. . .")
MenuSet()
def runAgain():
    runAg=input("want To Run Again Y/n:")
    while (runAg.lower() == "y"):
        if (platform.system() == "Windows"):
            print(os.system("cls"))
        else:
            print (os.system("clear"))
        MenuSet()
        runAg=input("want To Run Again Y/n:")
runAgain()
