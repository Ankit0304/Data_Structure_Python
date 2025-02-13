class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    
    def setDimensions(self,length,breadth):
        self.length=length
        self.breadth=breadth
    
    def showDimensions(self):
        print(f'length:{self.length}\nbreadth:{self.breadth}')
        
    def getArea(self):
        return self.length*self.breadth
    

length = int(input("Enter length:"))
breadth = int(input("Enter breadth:"))
r1=Rectangle(length,breadth)
r1.showDimensions()
print("Area of Rectangle: ",r1.getArea())