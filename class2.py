class Circle:
    def __init__(self,radius=0):
        self.radius=radius
    
    def setRadius(self,radius):
        self.radius=radius
        
    def getRadius(self):
        return self.radius
    
    def getArea(self):
        return 3.14*self.radius*self.radius
    
    def getCircumference(self):
        return 2*3.14*self.radius
    
    
c1=Circle()
radius=int(input("Enter radius:"))
c1.setRadius(radius)
print("Radius:",c1.getRadius())
print("Area of Circle : ",c1.getArea())
print("Circumference of Circle : ",round(c1.getCircumference(),2))
