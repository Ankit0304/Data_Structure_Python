class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def show(self):
        print(f'Name:{self.name}\nAge:{self.age}')
        
        
p1=Person("Ravi",30)
p2=Person("Deva",22)
p1.show()
p2.show()