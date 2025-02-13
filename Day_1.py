from array import *
a1 = array('i', [1, 2, 3, 4, 5])
print("Array is : ",a1)
print(type(a1))
for i in a1:
    print(i, end=' ')
    
#array methods
a1.append(4)
print("count of number:",a1.count(4))
a1.extend([1])
a1.fromlist([10,11,12])
print("Index of given number: ",a1.index(4))
a1.insert(5,5)
a1.pop(7)
a1.remove(12)
a1.reverse()
print(a1.tolist())
# a1.tounicode()
print("Reversed array: ",a1) 
    
     
 