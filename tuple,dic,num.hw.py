#####   TUPLE AND DICTIONARY AND NUMBERS

- TUPLE is the same as LIST, but values in the tuple is not changable
- TUPLE is immutable
- here we not change the values but execution of tuple is speed

# SETS
- it never follow the sequence.
- it is not support duplicate values.

s={23,45,32,45,67,89,98}
print(s) # o/p is not in same sequence
         # in the o/p is 45 is once
s[2]  # in set, indexing is not supporting because we dont have proper sequence       
s.pop()         
         
#### empty tuple
tuple = ()
print(tuple)

 ###############  creating tuple with elements
tuple = (1,123.87,65)
print(tuple)
        ######  brackets not required
tuple = 1,123.87,65
print(tuple)

##########  tuple with mixed datatypes
tuple = (234,'Hirekerur',67.09)
print(tuple)

################  nested tuple     #########  asked sir
tuple = ('Hirekerur',[1,2,3,4],'Haveri')
print(tuple)

#############  tuple unpacking method   #### ask sir
tuple = (123,'ram',40000,'company')
print(tuple)
empid,name,sallary,comname = tuple
print(empid)
print(name)
print(sallary)
print(comname)

#######################
tuple = (1,2,3,4,5) 
print(tuple[0])
print(tuple[1])
print(tuple[3])


###########  nested list
nest_tuple = ('THURSDAY',[100,200,300,400,500])
print(nest_tuple[0])
print(nest_tuple[0][3])
print(nest_tuple[0][5])
print(nest_tuple[1][3])
print(nest_tuple[1][4])

############### slicing list 
tuple = ('SUN','MON','TUE','WED','THU','FRI','SAT')
print(tuple[1:6])
print(tuple[:6])
print(tuple[0:6])
print(tuple[0:])
print(tuple[:])
print(tuple[-6:-3])
print(tuple[-6:])
print(tuple[-3:])
print(tuple[:])

###############      tuple elements are immutable
tuple = ('h','i','r','e','k','e','r','u','r')
print(tuple)
tuple[0]='r' # here not possible but list it is possible


tuple = ('h','v','e','r','i')
print(tuple)

###########concatination with tuple
tuple1=['W','E','L']
tuple2=['C','O','M','E']
print(tuple1+tuple2)

##################
print(('TEJU',) * 3)

################### DELETION METHOD NOT APPLICABLE TO TUPLES

tuple = ('A','P','P','L','E')
print(tuple.index('A'))
print(tuple.count('P'))

##############################
tuple = (1,2,3,4,5,6)
print(1 in tuple)
print(1 not in tuple)

#####################  iteration thru tuple elements
tuple = ('h','i','r','e','k','e','r','u','r')
for letters in tuple:
    print('letter is ->',letters)
    
    #####################################
tuple = (9,8,7,4,5,6,1,2,3)
print(max(tuple))
print(min(tuple))
print(sum(tuple))
print(sorted(tuple))    
print(len(tuple))

####################   DICTIONARIES

- create the dictionary by using lists or tuple
- dictionaries are faster than list.

t1=('a','b','c','d')
t2=(21,34,56,43)
list(zip(t1,t2))   # install pip for python




dictionary = {'spain' : 'madrid','usa' : 'vegas'}
print(dictionary.keys())
print(dictionary.values())

# getting values from keys
print(dictionary['spain'])

# gettting keys from values 
print(list(dictionary.keys())[list(dictionary.values()).index('madrid')])


dictionary['spain'] = "barcelona"    # update existing entry
print(dictionary)

dictionary['france'] = "paris"       # Add new entry
print(dictionary)

del dictionary['spain']              # remove entry with key 'spain'
print(dictionary)

print('france' in dictionary)        # check include or not

dictionary.clear()                   # remove all entries in dict

print(dictionary)






dict = {0:'Ram', 2:'Lakshman', 3:'Hanu'}
print(dict)
print(dict[0])
print(dict[3])
print(dict.get(4))
print(dict.get(2))

###########   updating value
dict = {0:'Ram', 2:'Lakshman', 3:'Hanu'}
print(dict)

dict[0]='Seeta'
print(dict)

dict[0]=('aaa','bbb')
print(dict)

##############    ADDING VALUE
dict = {0:'Ram', 2:'Lakshman', 3:'Hanu'}
print(dict)

dict[4]='JHG'
print(dict)

#############################
sq_dict = {1:1,2:4,3:9,4:16,5:25,6:36}
print(sq_dict)

print(sq_dict.pop(2))  ###  remove paerticular item
print(sq_dict)

print(sq_dict.popitem())   ######  it prints the last item(  arbitary item  )
print(sq_dict)

del sq_dict[1]
print(sq_dict)

###########################
sq_dict = {1:1,2:4,3:9,4:16,5:25,6:36}
print(sq_dict)

sq_dict.clear()
print(sq_dict)

del sq_dict
print(sq_dict)   #######  it produces an error message

######### creating new dictionary using comprehension
sqr={x : x*x for x in range(7)}
print()

##############  dictionary membership test
sq_dict = {1:1,2:4,3:9,4:16,5:25,6:36}
print(sq_dict)

print(1 in sq_dict)
print(5 in sq_dict)
print(10 in sq_dict)
print(25 in sq_dict)  #### 1 5 10 and 25 are keyvalues

#####   iterating through a dictionary
sq_dict = {1:1,2:4,3:9,4:16,5:25,6:36}
for i in sq_dict:
    print([i])
    print(sq_dict[i])
    
    print(len(sq_dict))
    print(sorted(sq_dict))
    
####################################################################
    ####   NUMBERS
    
value=100    #####   INT
print(type(value))
print(isinstance(value,int))
print(isinstance(value,float))
print(isinstance(value,complex))

value=100.50    ####  FLOAT
print(type(value))
print(isinstance(value,int))
print(isinstance(value,float))
print(isinstance(value,complex))

value=10+5j    ####   COMPLEX

print(type(value))
print(isinstance(value,int))
print(isinstance(value,float))
print(isinstance(value,complex))      
######################################################
print(10+3.4)
#####################

print(0B1101) ## B is binary 
print(0O23)   ## O is octal  (watch notes for calculation)
print(0XAB)   ## X is hexadecimal

############  TYPE CONVERSION
print(int(10.5))
print(float(10))
print(int(-20.45))

#########  python decimals
print(0.1+0.2)
print(1.20 * 2.50)

from decimal import Decimal as D
print(D('0.1') + D('0.2'))
print(D('1.2') * D('2.5'))

#################   Python fractions
from fractions import Fraction as F
print(F(1.5))
print(F(5))
print(F(1,5))

#######  Python math module
import math
print(math.pi)
print(math.cos(10))
print(math.log(10))
print(math.log10(10))
print(math.exp(10))
print(math.factorial(5))
print(math.sinh(10))
print(abs(-12.34))  ### sign part is ignored

########   python random value

import random
print('Random number -> ',random.randrange(5,15))
print('Random number -> ',random.randrange(5,15))
print('Random number -> ',random.randrange(5,15))
print('Random number -> ',random.randrange(5,15))
print('Random number -> ',random.randrange(5,15))  ###  repeat

import random
day=['sun','mon','tue','wed','thu','fri','sat']
print(random.choice(day))  ###  repeat

import random
day=['sun','mon','tue','wed','thu','fri','sat']
print(day)
random.shuffle(day)
print(day)
    
####  print random element
print(random.random())



 

from nltk.corpus import webtext













