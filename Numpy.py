
import numpy as np
 
# Creating array object
arr = np.array( [[ 1, 2, 3, 4, 5, 6],[ 7, 8, 9, 10, 11, 12]] )
                 
print(arr[0])
 
print("Array is of type: ", type(arr))
 
print("No. of dimensions: ", arr.ndim)
 
print("Shape of array: ", arr.shape)
 
print("Size of array: ", arr.size)
 
print("Array stores elements of type: ", arr.dtype)

print ("Largest element is:", arr.max())

print ("Smallest element is:", arr.min())

print("This is numpy zeros ",np.zeros((4,2)))

print("This is numpy Ones ",np.ones((1,2,3)))

print("This is reshaped array ",arr.reshape(6,2))

print("Logspace : ",np.logspace(2.0, 3.0, num=5, dtype = int , base = 10)) 

print("Linspace :",np.linspace(0, 2, 3))

print("Printing Flattened Array : ", arr.flatten() )

print("Sorted array:",np.sort(arr))

print("Matrix :",np.matrix(arr))






