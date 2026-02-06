#indexing and slicing in numpy

#indexing slicing 
import numpy as np
arr_1d= np.array([1,2,3])
print(arr_1d[1])

#  slicing
import numpy as np
arr_1d= np.array([1,2,3])
print(arr_1d[0:len(arr_1d)])   #len(arr_id) is length of character


import numpy as np
arr_1d= np.array([1,2,3,4,5,6,7,8,9])
print(arr_1d[1])
print(arr_1d[1:])
print(arr_1d[:1])
print(arr_1d[1:-1])
print(arr_1d[1:10:2])

#fancy indexing 
#selectin multiple eliments at once 
import numpy as np
arr_1d= np.array([1,2,3,4,5,6,7,8,9])
print(arr_1d[1:10:2])



# filtering data
# bolean masking 
import numpy as np
arr_1d= np.array([1,2,3,4,5,6,7,8,9])
print(arr_1d[arr_1d%2 ==0])



#reshaping and manipulating array
# its use to changing the dimantion of array without modifying the data
#dimantion should same 

import numpy as np
arr_1d= np.array([1,2,3,4,5,6,7,8,9])
change=arr_1d.reshape(3,3)
print(change)

  
#falting array 
# thre are two types 
# 1. ravel- return view
# 2. flatten - return copyes
#we use it when we need to cnvert multi d array into 1 d array

import numpy as np
arr = np.array([[1,2,3],
               [4,5,6]])

print(arr.ravel())
print(arr.flatten())