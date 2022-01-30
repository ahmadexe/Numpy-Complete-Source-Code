import numpy as np
listarray = np.array([[[[1,2,3,4],[5,6,7,8],[9,3,4,5]]]])
print(listarray)

print(listarray.dtype) #tells data type (bits)
print(listarray.shape) #Tells number of rows and numbers of column
print(listarray.size) #total elements in the array
print(listarray[0,0]) #Specify object at 0th row and 0th column
print(listarray.ndim) #tells dimension