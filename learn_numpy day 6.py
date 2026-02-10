# handling missing  and special Values

#NON - not a number

#find the missing value 

import numpy as np
arr = np.array([1,2,3,np.nan,4,5,np.nan,3])
print(np.isnan(arr))


#replacing the value 

#nan_to_num (array,nan=value) default value = 0 

import numpy as np
arr = np.array([1,2,3,np.nan,4,5,np.nan,3])
arr1 =np.nan_to_num(arr,nan=100)
print(arr1)

#for infinite value like 10/10000 and 1/0 like that 
# we use np.isinf() 

import numpy as np 
arr = np.array([1,2,np.inf,45])
arr1= np.isinf(arr)
print(arr1)

#for changing the value 
import numpy as np 
arr = np.array([1,2,np.inf,45])
okay = np.nan_to_num(arr,posinf=100 ,neginf=0)
print(okay) 