class Empoyee:
    def __init__(self,empid=None,empname=None,empsal=None):
        self.empid=empid
        self.empname=empname
        self.empsal=empsal
    def setempid(self,empid):
        self.empid=empid
    def getempid(self):
        return self.empid
    def setempname(self,empname):
        self.empname=empname
    def getempname(self):
        return self.empname
    def setempsal(self,empsal):
        self.empsal=empsal
    def getempsal(self):
        return self.empsal
    
e1=Empoyee()
e1.setempid(101)
e1.setempname("Ravi")
e1.setempsal(50000)
print(e1.getempid(),e1.getempname(),e1.getempsal())
e2=Empoyee(102,"Raj",60000)
print(e2.getempid(),e2.getempname(),e2.getempsal())
e3=Empoyee()
print(e3.getempid(),e3.getempname(),e3.getempsal())