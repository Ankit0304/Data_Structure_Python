class Team:
    def __init__(self):
        self.lst=[]
    
    def inplst(self):
        num_members=int(input("Enter number of members :"))
        for i in range(num_members):
            name=input("Enter name of team member:")
            self.lst.append(name)
            i+=1
    
    def display(self):
        print("Team members are:")
        for i in self.lst:
            print(i)

    def show(self):
        print(self.lst)
    
t1=Team()
t1.inplst()
t1.display()
t1.show()
    
    
        