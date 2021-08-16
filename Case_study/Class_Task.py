class Task:
    def __init__(self,taskid,name,description,status,priority,notes,bookmark,ownerid,createrid,createdon,modifiedon):
        self.taskid=taskid
        self.name=name
        self.description=description
        self.status=status
        self.priority=priority
        self.notes=notes
        self.bookmark = bookmark
        self.ownerid = ownerid
        self.createrid = createrid
        self.createdon = createdon
        self.modifiedon = modifiedon


