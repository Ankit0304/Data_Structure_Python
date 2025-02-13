class Test:
     x=5 # class object variable
     def __init__(self,y,z):    
         self.y=y # instance object variable
         self.z=z
    
     def display(self):
        print("this is display method")
     @staticmethod
     def show():
        print("this is show method")
     @classmethod
     def new(cls):
        print("this is new method",cls.x)
    
t1=Test(3,4)
print(t1.x , t1.y, t1.z)
Test.show()
t1.display()
Test.new()
t1.show()
# t2=Test()
