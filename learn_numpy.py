#diff b/w list in python and array in numpy
#list in python 
paython_list = [1,2,3,4,5,6]
print(paython_list)


#array in numpy
import numpy as np
numpy_array = np.array([1,2,3,4,5,6])
print(numpy_array)


# array
#one-D-array (one dimensional array )
import numpy as np
array_1d = np.array([10,20,30,40,50])
print(array_1d) 


#two-D-array ( 2 dimensional array)
import numpy as np
array_2d = np.array([
                    [2,3,4],
                    [5,4,6],
                    [8,9,10]
                    ])

print(array_2d)


#multi - dimensional array 

import numpy as np

print("START")
print(type(np))

multi_array = np.array([
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [1,2,3],
        [4,5,6]
    ]
])

print(type(multi_array))
print(multi_array)


#createing array

import numpy as np 
arr = np.array("kunal")
print(arr)

print("this is the example of how to create array")


#creating array with deafault values zero 
# their is a bulid-in called zeroes funtion it have default values zero .

import numpy as np
zero=np.zeros(3)
print(zero)


#ones(shape)
#it will print only default values
import numpy as np
one = np.ones((3,3))
print(one)



#full(shape)
#it will print the given values also 
import numpy as np
fulll=np.full((3,3),7)
print(fulll)



#creating sequences number in numpy
#arrange()
#arange(start,stop,step)

import numpy as np
range = np.arange(1,11,2)
print(range)


#creating identity matrix
#eye(size)

import numpy as np
identity_m=np.eye(3)
print(identity_m)