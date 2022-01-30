import numpy as np
array = np.array([[1,2,3],[4,5,6]])



print(array)
print(array.ndim)
x = array.prod(axis=0)
print(x)
y = array.sum(axis=1)
print(y)



# #how to transpose same in pandas
# print(array.T)

# x = array.flat
# print(x)
# for item in x:
#     print(item)


