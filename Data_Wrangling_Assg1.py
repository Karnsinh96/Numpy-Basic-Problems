#1. Create a null vector of size 10 but the fifth value which is 1.
import numpy as np
print("Create a null vector of size 10 but the fifth value which is 1.")
vec=np.zeros(9)
#print(vec)
vec[4]=1
print(vec)

#2. Create a vector with values ranging from 10 to 49.
print("\nCreate a vector with values ranging from 10 to 49.")
vec=np.arange(10,50)
print(vec)

#3.Create a 3x3 matrix with values ranging from 0 to 8
print("\nCreate a 3x3 matrix with values ranging from 0 to 8")
vec=np.arange(9).reshape(3,3)
print(vec)

#4.Find indices of non-zero elements from [1,2,0,0,4,0]
print("\nFind indices of non-zero elements from [1,2,0,0,4,0]")
arr = np.array([1,2,0,0,4,0])
ind= np.nonzero(arr)
print ("Indices of non zero elements : ", ind)

#5. Create a 10x10 array with random values and find the minimum and maximum values.
print("\nCreate a 10x10 array with random values and find the minimum and maximum values.")
arr = np.random.randint(100,size=(10,10)) 
print(arr)
print("Minimum value of element is:- ",np.min(arr))
print("Maximum value of element is:- ",np.max(arr))

#6. Create a random vector of size 30 and find the mean value.
print("\nCreate a random vector of size 30 and find the mean value.")
vec=np.random.rand(30)
print(vec)
print("The Mean Value is:- ",np.mean(vec))