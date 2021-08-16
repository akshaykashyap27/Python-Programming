from user_DB import insertUser
from task_DB import insertTask
from task_DB import updatePriority
from task_DB import updateNotes
from task_DB import updateBookmark
from task_DB import updateStatus
from task_DB import AssignTask
from report import GetAllTasksUser
from report import GetAllTasksBasedOnStatus
from report import GetAllTasks
from User import User
from Class_Task import Task
from datetime import datetime
ans=True
while ans:
    print ("""
    1.Create a user
    2.Create a task
    3.Update Priority
    4.Update Notes
    5.Update Bookmark
    6.Update Status of task
    7.Get All tasks for a given user
    8.Get All tasks based on status
    9.Get ALl tasks without any condition
    10.Assign Task to User
    """)
    ans=input("What would you like to do? ")
    if ans=="1":
      userid=input("Enter userid:")
      username=input("Enter username:")
      contactno=input("Enter contact number:")
      role=input("Enter job role:")
      dob=datetime.now()
      createdon=datetime.now()
      modifiedon=datetime.now()
      email=input("Enter the user e-mail ID:")
      u=User(userid,username,contactno,role,dob,createdon,modifiedon,email)
      insertUser(u)

    elif ans=="2":
        taskid = input("Enter taskid:")
        name = input("Enter name:")
        description = input("Enter task description:")
        status = input("Enter task status:")
        priority = 0
        notes = input("Enter any notes:")
        bookmark = input("Enter any bookmarks:")
        ownerid = 0
        createrid= input("Enter createrid:")
        createdon = datetime.now()
        modifiedon = datetime.now()

        t = Task(taskid, name, description, status, priority, notes, bookmark, ownerid, createrid, createdon, modifiedon)
        insertTask(t)

    elif ans=="3":
        priority=input("Enter priority to be updated")
        taskid=input("Enter taskid for which priority to be updated")
        updatePriority(priority,taskid)

    elif ans=="4":
        notes=input("Enter notes to be updated")
        taskid=input("Enter taskid for which updation is required")
        updateNotes(notes,taskid)

    elif ans=="5":
        bookmark = input("Enter bookmark to be updated")
        taskid = input("Enter taskid for which updation is required")
        updateBookmark(bookmark, taskid)


    elif ans=="6":
        status=input("Enter the status of a task")
        taskid=input("Enter taskid for which status has to be updated")
        updateStatus(status,taskid)

    elif ans=="7":
        userid=input("Enter the userid:")
        print(GetAllTasksUser(userid))

    elif ans=="8":
        status=input("Enter completed/not completed:")
        print(GetAllTasksBasedOnStatus(status))

    elif ans=="9":
        print(GetAllTasks())

    elif ans=="10":
        taskid=input("Enter taskid for which user should be assigned:")
        userid=input("Enter userid to be assigned to the task")
        AssignTask(userid,taskid)

    elif ans !="":
        print("\n Not a Valid Choice Try again")

