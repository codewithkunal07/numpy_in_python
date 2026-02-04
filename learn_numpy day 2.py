#array properties and opreations

#shape
import numpy as np
arr = np.array([[1,2,3],
               [4,5,6]])

print(arr.shape)



#size
import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
print(arr.size)

#ndim
#its use for knowing the dimantion
import numpy as np

arr_1d= np.array([1,2,3])
arr_2d= np.array([[1,2,3],[3,4,5]])
arr_3d= np.array([[[1,2],[3,4],[5,6]]])

print(arr_1d.ndim)
print(arr_2d.ndim)
print(arr_3d.ndim)

#dtype
#for knowing the data type  
import numpy as np

arr_1d= np.array([1,2,3])
print(arr_1d.dtype)



#astype 
#its use for converting the datatype into other datatype
import numpy as np

arr_1d= np.array([1.1,2.2,3.3])
change=arr_1d.astype(int)
print(change)


#arthmatical opreations on numpy
#for addition

import numpy as np

arr_1d= np.array([1,2,3])
arr=arr_1d+5
print(arr)


#for multiplication
import numpy as np

arr_1d= np.array([1,2,3])
arr=arr_1d*5
print(arr)

#for substraction
import numpy as np

arr_1d= np.array([10,20,30])
arr=arr_1d-5
print(arr)

#aggrigation functions

#sum
import numpy as np

arr_1d= np.array([10,20,30])
arr=np.sum(arr_1d)
print(arr)


# avg
import numpy as np

arr_1d= np.array([10,20,30])
arr=np.mean(arr_1d)
print(arr)


# min
import numpy as np

arr_1d= np.array([10,20,30])
arr=np.min(arr_1d)
print(arr)

# max
import numpy as np

arr_1d= np.array([10,20,30])
arr=np.max(arr_1d)
print(arr)

# stan
import numpy as np

arr_1d= np.array([10,20,30])
arr=np.std(arr_1d)
print(arr)

# var
import numpy as np

arr_1d= np.array([10,20,30])
arr=np.var(arr_1d)
print(arr)