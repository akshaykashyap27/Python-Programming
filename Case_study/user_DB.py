import mysql.connector
from datetime import datetime
from User import User

def connectToDB():
        mydb = mysql.connector.connect(host="localhost", user="root", password="Ak99#40*72", database="jobtracking")
        return mydb


def insertUser(user):
        mydb = connectToDB()
        mycursor = mydb.cursor()
        sql = "insert into user (username,contactno,role,dob,createdon,modifiedon,email) values(%s,%s,%s,%s,%s,%s,%s)"
        val = (user.username, user.contactno, user.role,user.dob,user.createdon,user.modifiedon,user.email)
        mycursor.execute(sql, val)
        mydb.commit()
        mydb.close()











