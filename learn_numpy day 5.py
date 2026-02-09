#brodcasting and vectorization

# apply 10% discount on evry customer salary 
import numpy as np 
prices= np.array([200,120,330,340,539])
discount = 10
final_price = prices-(prices * discount/100)
print(final_price)



import numpy as np 
prices= np.array([200,120,330,340,539])
okay = prices*2
print(okay)


#brodcasting with arrays 
import numpy as np
arr = np.array([[1,2,3],   # 2d amrix
               [4,5,6]])

arr2 = np.array([1,2,3])   # 1d matrix

okay  = arr+ arr2
print(okay)

# import numpy as np
# arr = np.array([[1,2,3],  
#                [4,5,6]])

# arr2 = np.array([1,2])   
# okay = arr+ arr2
# print(okay)

#it will  show the error becouse of shape 



#vectorization 
#addition
import numpy as np
arr = np.array([1,2,3])  
arr2 = np.array([4,5,6])

add = arr+arr2
print(add)

#multiplication
import numpy as np
arr = np.array([1,2,3])  
arr2 = np.array([4,5,6])

add = arr*arr2
print(add)
