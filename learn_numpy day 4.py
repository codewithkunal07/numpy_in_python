#advance numpy
#reshaping and manipulating array


#insert(array,index,value,asix=none) 
# array - our data
# index - where we wanna insert our new data
# value - what we wanna insert

import numpy as np
arr= np.array([1,2,3,5,6,7,8])
new=np.insert(arr,3,5)
print(new)
print('end')

#inserting the data in 2d array 
import numpy as np
arr= np.array([[1,2],[4,5]])
new=np.insert(arr,3,[7,8])
print(new)

print('end')


#append
import numpy as np
arr= np.array(('kunal'))
app=np.append(arr,('rajput'))
print(app)

#concatinate
import numpy as np
arr1= np.array([6,7,8,9])
arr2= np.array([1,2,3,4])
arr3=np.concatenate((arr1,arr2))
print(arr3)


#deleting  
import numpy as np
arr= np.array([1,2,3,5,6,7,8])
new=np.delete(arr,0)
print(new)

#stacking 

#horizontally
#vatrically

# vstack()-rowwise
# hstack()-columwise

import numpy as np
arr1= np.array([6,7,8,9])
arr2= np.array([1,2,3,4])

arr3=np.vstack((arr1,arr2))    # print(np.vstack((arr1,arr2)))
print(arr3)
arr4=np.hstack((arr1,arr2))    #print(np.hstack((arr2,arr2)))
print(arr4)


#spliting
# 1.split
# 2.hsplit
# 3.vsplit

import numpy as np
arr= np.array([6,7,8,9,2,3,4,5,6])
arr2=np.split(arr,3)
print(arr2)

