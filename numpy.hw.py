##########    NUMPY    28/12/2018
## array= similar type of elements

# FUNCTIONS ARE  # np.array # np.dtype # np.arange # np.reshape # np.shape # size # itemsize  #####   np.ones
# np.zeros # slice and   type of

import numpy as np
a=np.array([1,2,3])
print(a)

a=np.array([1,2,3],dtype=float)
print(a)

a=np.array([1,2,3],dtype=float,ndmin=2)
print(a)

a=np.array(([1,2],[3,4]),dtype=int)
print(a)

a=np.array(([1,2],[3,4],[5,6],[7,8]),dtype=int)
print(a)

a=np.array(([1,2,3],[4,5,6]),dtype=int)
print(a)

import numpy as np
data = np.array([(1,'Abhi',92),(2,'Akash',87),(3,'Amar',80)],dtype=data)
dt=np.dtype([('Number','int'),('Name','S10'),('Marks','int')])
print(data)

import numpy as np
student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')]) 
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student) 
print (a)

# an array of evenly spaced numbers 
import numpy as np 
a = np.arange(101)
print (a)

###########################  29/12/18
import numpy as np 
a = np.arange(0,100,2)
print (a)
####################

import numpy as np 
a = np.arange(1,17)
print (a)
b=np.reshape(a,[4,4])
print(b)
###   b.shape
###   b.itemsize  4 butes(integer)
############################
import numpy as np 
x = np.array([1,2,3,4,5], dtype = np.int64) 
print (x)
###   x.itemsize    o/p is 8    (8byte=64bits)
###   x.size        o/p is 5  size of the array

import numpy as np
a = np.zeros(9)
b=np.reshape(a,[3,3])
print(b)
############################
import numpy as np
a = np.ones(9)
b=np.reshape(a,[3,3])
print(b)
##############################  1 to 20 5*4



#################
help(np.arange)

print('*')
print('**')
print('***')
print('****')
print('*****')
######################
print('*' * 4)
##################


#########################    home work
import numpy as np
a=np.array([1,2,3,4,5])
print(a)

#############  more than one dimensional
import numpy as np
a=np.array([[1,2], [5,6],[7,8]])
print(a)

################  minimum dimensions
import numpy as np
a=np.array([1,2,3,4],ndmin=2)
print(a)
    # or
import numpy as np
a=np.array([[1,2,3,4,5]])
print(a)
#########

import numpy as np
a=np.array([1,2,3,4],ndmin=3)
print(a)
    ###  or
import numpy as np
a=np.array([[[1,2,3,4,5]]])
print(a)

### dtype parameter
import numpy as np
a=np.array([1,2,3,4],dtype=complex)
print(a)

import numpy as np
a=np.array([1,2,3,4],dtype=int)
print(a)

import numpy as np
a=np.array([1,2,3,4],dtype=float)
print(a)

#####  using array-scalar type
import numpy as np
a=np.dtype(np.int8) #####   Byte (-128 to 127)
print(a)
####        NUMPY DATATYPES
import numpy as np
a=np.dtype(np.int16)  ###   Integer (-32768 to 32767)
print(a)

import numpy as np
a=np.dtype(np.int32)  ####  Integer (-2147483648 to 2147483647)
print(a)

import numpy as np
a=np.dtype(np.int64)   ###  Integer (-9223372036854775808 to 9223372036854775807)
print(a)

# uint8 - Unsigned integer (0 to 255)	
# uint16 - Unsigned integer (0 to 65535)
# uint32 - Unsigned integer (0 to 4294967295)
# uint64 - Unsigned integer (0 to 18446744073709551615)
# float_  Shorthand for float64
# float16 - Half precision float: sign bit, 5 bits exponent, 10 bits mantissa
# float32 - Single precision float: sign bit, 8 bits exponent, 23 bits mantissa
# float64 - Double precision float: sign bit, 11 bits exponent, 52 bits mantissa
# complex_  Shorthand for complex128
# complex64 - Complex number, represented by two 32-bit floats (real and imaginary components)
# complex128 - Complex number, represented by two 64-bit floats (real and imaginary components)

#################

###int8, int16, int32, int64 can be replaced by equivalent string 'i1', 'i2','i4', etc.
import numpy as np
a=np.dtype('i1')
print(a) 

import numpy as np
a=np.dtype('i3')
print(a) 

# using endian notation 
import numpy as np 
a = np.dtype('>i4') 
print (a)
# '<' means that encoding is little-endian (least significant byte is stored in smallest address).
# '>' means that encoding is big-endian (most significant byte is stored in smallest address).
import numpy as np 
a = np.dtype('<i4') 
print (a)

####  creating structured data type
import numpy as np
a=np.dtype([('age',np.int8)])
print(a)

####  combine structured data type to ndarray object
import numpy as np
dt=np.dtype([('age',np.int16)])
a=np.array([10,20,30],dtype=dt)
print(a)

import numpy as np
dt=np.dtype([('age',np.int16)])
a=np.array([10,20,30],dtype=dt)
print (a['age'])

# structured data type called student with a string field 'name',
 #                           an integer field 'age' and a float field 'marks'.
import numpy as np
dt=np.dtype([('name','S10'),('age','i1'),('weight','f4')])
print(dt)

import numpy as np              #####  ask sir
dt=np.dtype([('name','S10'),('age','i1'),('weight','f4')])
a=np.array([('aaa',20,10),('xyz',30,40)],dtype=dt)
print(a)    ##  string with 10 byte, integer with one byte,float with four bute

## 'b' − boolean  'i' − (signed) integer   'u' − unsigned integer
##  'f' − floating-point   'c' − complex-floating point   'm' − timedelta
##  'M' − datetime       'O' − (Python) objects    'S', 'a' − (byte-)string
##   'U' − Unicode         'V' − raw data (void)

##    ndarray.shape & reshape
import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8]])
print(a.shape)

import numpy as np
a=np.array([[1,2,3],[4,5,6]])
a.shape=(2,3)
print(a)


import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=a.reshape(3,2)
print(b)

# an array of evenly spaced numbers 
import numpy as np 
a = np.arange(24) 
print (a)

import numpy as np 
a = np.arange(0,100,2)
print (a)

import numpy as np 
a = np.arange(1,100,3)
print (a)

import numpy as np 
a = np.arange(24) 
print (a)
b=a.reshape(2,4,3)
print(b)
print(b.ndim)  # 3 dimensional array

###  numpy.size and numpy.itemsize
import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print(a)
print(a.size)
print(a.itemsize)


# dtype of array is int8 (1 byte) 
import numpy as np 
x = np.array([1,2,3,4,5], dtype = np.int8) 
print(x.itemsize)

# dtype of array is now float32 (4 bytes) 
import numpy as np 
x = np.array([1,2,3,4,5], dtype = np.float32) 
print (x.itemsize)

##  The following example shows the current values of flags.
import numpy as np 
x = np.array([1,2,3,4,5]) 
print(x.flags)

##   numpy.empty
import numpy as np 
x = np.empty([3,2], dtype = int) 
print (x)

import numpy as np 
x = np.empty([3,2], dtype = float) 
print (x)

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































