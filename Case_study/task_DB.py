import mysql.connector
from Class_Task import Task
from datetime import datetime
import smtplib


def connectToDB():
    mydb = mysql.connector.connect(host="localhost", user="root", password="password", database="jobtracking")
    return mydb

def insertTask(task):
    mydb = connectToDB()
    mycursor = mydb.cursor()
    sql = "insert into task (taskid,name,description,status,notes,bookmark,createrid,createdon,modifiedon) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (task.taskid, task.name,task.description, task.status,task.notes,task.bookmark,task.createrid,task.createdon,task.modifiedon)
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close()

def updatePriority(priority,taskid):
    mydb = connectToDB()
    mycursor = mydb.cursor()
    sql = "UPDATE task set priority=%s where taskid=%s"
    val = (priority, taskid)
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close()

def updateNotes(notes,taskid):
    mydb = connectToDB()
    mycursor = mydb.cursor()
    sql = "UPDATE task set notes=%s where taskid=%s"
    val = (notes, taskid)
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close()

def updateBookmark(bookmark,taskid):
    mydb = connectToDB()
    mycursor = mydb.cursor()
    sql = "UPDATE task set bookmark=%s where taskid=%s"
    val = (bookmark, taskid)
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close()

def updateStatus(status,taskid):
    mydb = connectToDB()
    mycursor = mydb.cursor()
    sql = "UPDATE task SET status=%s WHERE taskid=%s"
    val = (status, taskid)
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close()

def AssignTask(userid,taskid):
    mydb = connectToDB()
    mycursor = mydb.cursor()
    sql="UPDATE task SET ownerid=%s WHERE taskid=%s"
    val=(userid,taskid)
    mycursor.execute(sql, val)
    session = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    session.login("s.akshay1999@gmail.com", "password")
    message = "Hello!! You have been assigned a task. Please complete it ASAP"
    session.sendmail("s.akshay1999@gmail.com", ReceiverEmail(userid), message)
    session.quit()
    mydb.commit()
    mydb.close()

def ReceiverEmail(userid):
    mydb = connectToDB()
    mycursor = mydb.cursor()
    sql="SELECT email FROM user WHERE userid=%s"
    val=(userid,)
    mycursor.execute(sql, val)
    for i in mycursor:
        return i








