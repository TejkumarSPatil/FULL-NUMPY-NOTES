####  numpy.arange

they are six ways to creating the array in numpy:
    they are- array, linspace, logspace, arange, zeros and ones.

from numpy import *
arr=array([2,4,5,6,8,4,9])
print(arr)
print(arr.dtype)
print(arr.ndim) 

from numpy import *
arr=array([2,4,5,6,8,4,9.0])   # if 1 value is float in the array, all values automatically converted to float
print(arr)
print(arr.dtype)


from numpy import *
arr=array([2,4,5,6,8,4,9.0],int)
print(arr)

import numpy as np
arr=np.array([2,3,6,9,4])
print(arr)


from numpy import *
arr=array([2,4,5,6,8,4,9],float)
print(arr)



##  arange

import numpy as np
a=np.arange(9)
print(a)

import numpy as np
a=np.arange(9,dtype=float)
print(a)

import numpy as np
a=np.arange(0,10,2)
print(a)



####   numpy.linspace(linearly spaced)Return numbers spaced evenly on a even scale in a specified interval)

import numpy as np
a=np.linspace(1,100,10)  # 10 means parts ( one to hundred is divided into ten parts)
print(a)
print(a[3])   # getting index value


from numpy import *
b=np.linspace(1,10,20)
print(b)

import numpy as np
a=np.linspace(1,100,10,retstep=True)
print(a)    ####  o/p 11.0 is the interval

import numpy as np
a=np.linspace(1,100,10,endpoint=False)
print(a) ##  o/p  last value 100 is not there




#####    numpy.logspace(Return numbers spaced evenly on a log scale.)
from numpy import *
b=np.logspace(1,10,20) # it starts from 10^1  to  10^10   divided into 20 parts
print(b)
b[1] #first value 
b[19] # last value

import numpy as np
a=np.logspace(1.0,2.0,num=10)
print(a)

import numpy as np
a=np.logspace(1,10,num=10,base=2)
print(a)





#####       NumPy - Indexing & Slicing
import numpy as np
a=np.arange(10)
print(a)
s=slice(2,7,2)
print (a[s])
 ##  When this slice object is passed to the ndarray, a part of it starting with index 2 up to 7 with a step of 2 is sliced.

#####   or
import numpy as np 
a = np.arange(10) 
b = a[2:7:2] 
print (b)

# slice single item 
import numpy as np 
a = np.arange(10) 
b = a[4] 
print(b)

# slice items starting from index 
import numpy as np 
a = np.arange(10) 
print(a[2:])

# slice items between indexes 
import numpy as np 
a = np.arange(10) 
print(a[2:5])



import numpy as np 
b = np.array([[1,2,3],[3,4,5],[4,5,6],[7,8,9],[10,11,12]])
print(b)
print(b.ndim)
print(b.size)  # total number of elements
c=b.reshape(1,15)
c=b.flatten()  # converting 2 dimensional to singke dimensional
print(c)
print(c.ndim)

##  b.min()
##  b.max()
##  b[0:]
##   b[4].size
##  b[1:]
##  b[3:]  upto 3rd row  rows deleted
##  b[:3]  after 3rd allrow all rows are deleted
##  b[2:4]  except 2nd and 3th row all rows deleted [2:4] 4 is exclusive
##  b[1,1] o/p is 4 (comma)
##   b[1,0]  o/p is 3
##  b[4,2]   o/p is 12

###   b[1,2],b[2,2]  o/p is (5,6)

#     b[0,0],b[1,0],b[2,0],b[3,0],b[4,0]   getting 1st column

###  b[(0,1,2),(2,2,2)]    o/p is array([3, 5, 6])
###  b[(3,4,3),(2,1,0)]    o/p is array([ 9, 11,  7])

###    b[1,(0,1,2)]  or  b[1,0:]   o/p is  array([3, 4, 5])

#####   b[b>5] o/p is, array([ 6,  7,  8,  9, 10, 11, 12])

#####   np.nonzero(b>5) 
o/p is,  (array([2, 3, 3, 3, 4, 4, 4], dtype=int32),
          array([2, 0, 1, 2, 0, 1, 2], dtype=int32))

#####   b[b<5]
#####   b>5   it is boolean formate
####   b[b%5==0]

#####################################################################
#  matrices
import numpy as np 
m=matrix('1 2 4 ; 4 6 9 ; 4 1 9')
print(m)
print(diagonal(m))
m.max()
m.min()
m.sum()

x=matrix('1 2 4 ; 4 6 9 ; 4 1 9')
y=matrix('1 2 4 ; 4 6 9 ; 4 1 9')
result=matrix('0 0 0 ; 0 0 0 ; 0 0 0 ')
print(x+y)
print(x*y)

# matrix is different from array
 
for i in range(len(x)):
    for j in range(len(y)):
        for k in range(len(y)):
            result [i][j] +=x[i][k]*y[k][j]
print('matrix 1 : 3x3')
for r in x:
    print(r)
    
print('matrix 2 : 3x3')
for r in y:
    print(r)    

print('matrix multiplication : 3x3')
for r in result:
    print(r)        
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
#######################################################################

import numpy as np 
a = np.array(([10,20,30]),dtype=int)
b = np.array(([40,50,60]),dtype=int)
print(a+b)



import numpy as np 
x = np.array([1,2,3,4,5], dtype = np.int64) 
print (x)
###   x.itemsize    o/p is 8    (8byte=64bits)
###   x.size    

import numpy as np 
x = np.array([1,2,3,4,5]) 
print (x)
###   x.itemsize    o/p is 4   (4byte=32bits)
###   x.size   


##   numpy.empty
import numpy as np 
x = np.empty([3,2], dtype = int) 
print (x)

import numpy as np 
x = np.empty([3,2], dtype = float) 
print (x)


# operation of array
import numpy as np
a=np.array([4,5,7,3,4])
print(a)
add=a+5     # adding 5 to all elements
print(add)

a=np.array([4,5,7,3,4])
print(a)
a.sum()  # sum of the array 
sin(a)
cos(a)
log(a)
sqrt(a)
a**2   # square of the array
min(a)
max(a)
sum(a)
sort(a)  # ascending order


# concatinate the two array.
import numpy as np
a1=np.array([4,5,7,3,4])
a2=np.array([3,4,5])
print(concatenate([a1,a2]))    


# with the help of one array create another array
import numpy as np
a=np.array([4,5,7,3,4])
print(a)
b=a
print(b)    
id(a)
id(b) # both have same memory location, for different memory location below one


import numpy as np
a=np.array([4,5,7,3,4])
print(a)

b=a.view()
print(b)
id(a)
id(b)

# shallow copy

import numpy as np
a=np.array([4,5,7,3,4])
print(a)
a[1]=23
print(a)
b=a.view()
print(b)   # if we change the a array element, automatically changed b array element
id(a)
id(b)

# deep copy= two different array, they not link each other

import numpy as np
a=np.array([4,5,7,3,4])
b=a.copy()
a[1]=23
print(a)
print(b)   # if we change the a array element, not changed b array element
id(a)
id(b)





## numpy.zeros
# array of five zeros. Default dtype is float 
import numpy as np 
x = np.zeros(5) 
print(x)

import numpy as np 
x = np.zeros(5, dtype = np.int) 
print(x)

# custom type 
import numpy as np 
x = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4')])  
print(x)

###   numpy.ones
# array of five ones. Default dtype is float 
import numpy as np 
x = np.ones(5) 
print(x)

import numpy as np 
x = np.ones([2,2], dtype = int) 
print(x)



# shape and reshape
import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8]])
print(a.shape)

import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=a.reshape(3,2)
print(b)



import numpy as np 
a = np.arange(24) 
print (a)
b=a.reshape(2,4,3)
print(b)
print(b.ndim)  # 3 dimensional array




















from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()








