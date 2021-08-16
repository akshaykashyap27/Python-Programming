import mysql.connector

def connectToDB():
    mydb = mysql.connector.connect(host="localhost", user="root", password="Ak99#40*72", database="jobtracking")
    return mydb

def GetAllTasksUser(userid):
    mydb = connectToDB()
    mycursor = mydb.cursor()
    sql = "SELECT user.username as user,task.name as taskName,task.description FROM user INNER JOIN task ON user.userid=task.ownerid"
    mycursor.execute(sql)
    result=mycursor.fetchall()
    for i in result:
        return i

def GetAllTasksBasedOnStatus(status):
    mydb = connectToDB()
    mycursor = mydb.cursor()
    sql = "SELECT name,description FROM task WHERE status LIKE %s"
    val=(status,)
    mycursor.execute(sql,val)
    result=mycursor.fetchall()
    for i in result:
        return i

def GetAllTasks():
    mydb = connectToDB()
    mycursor = mydb.cursor()
    sql = "SELECT ownerid,name,description FROM task"
    mycursor.execute(sql)
    result=mycursor.fetchall()
    return result