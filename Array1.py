# sort the array values
arr1=[54,3,63,4,76,34,6,7,23,65,32]
print("unsorted Array1: ",arr1)
arr1.sort()
print("sorted Array1: ",arr1)

# heterogeneous elements remove non-int values
arr2=[1, "a", [3.14], 2, "hello", 5]
print("Heterogeneous Array2: ",arr2)
arr2_int=[x for x in arr2 if type(x)==int]
print("Array2 with only integers: ",arr2_int)

# calculate the average of elements of a list
arr3=[10, 20, 30, 40, 50]
sum=0
arr_len=len(arr3)
for i in arr3:
    sum+=i
average=sum/arr_len

print("Average of the list: ",average)

# first N prime numbers
arr4=[]
n=int(input("Enter the number of prime numbers: "))
for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        arr4.append(i)
    if len(arr4)==n:
        break
print(f"First {n} prime numbers: ",arr4)

# n terms of a Fibonacci series
arr5=[]
n=int(input("Enter the number of terms in Fibonacci series: "))
a,b=0,1
for i in range(n):
    arr5.append(a)
    a,b=b,a+b
print(f"First {n} terms of Fibonacci series: ",arr5)