import keyword
print(keyword.kwlist)

#data type:
'''long data type only available in python 2 not applicable in python 2. version
# int value can be represent in 4 form

#decimal form(base-10)
# in this allowed digits are 0 to 9

#binary form(base-2)
#in this allowed values are 0 and 1 but 0 with small b or capital B
'''
d = 0B1111
print(d)

'''#octal form(base-8)
# in this allowed values are 0 to 7 but 0with small o or with capital O
'''
e = 0o123
print(e)

#f = 0o783
#print(f)
# it will get error because 8 is not between 0 to 7

#Hexa decimal(base-16)
# allowed values are 0 to 9 or A to F but

g = 0X10
print(g)
h = 0XFace
print(h)
i = 0XBeef
print(i)

# 2
# base conversion functions:
bin(15)
bin(0o123)
bin(0XFace)
oct(100)
oct(0XFace)
hex(1000)
hex(0b101)
hex(0o1)

# 3
# float data type:

#integral value we can only represented in hexa,bin,octal and decimal form but floating values
# we can only represent in decimal we can not use hexa, binary and octal form

f = 1.235
print(f)
#f= 0B1.235
#it will get error because it is binary form
# f =0X23.45
#f = 0B1.011
# f = 0o123.34

#exponetial or scintific notation only applicable only for floating values

f = 1.2e3
print(f)
f = 1.2e16
print(f)


# 4
# complex data type:
x = 10 + 20j
print(type(x))
print(x)
print(x.real)
print(x.imag)
x = 10.5 + 20j
x = 10.5 + 20.5j
x = 0B111 + 20j
# x = 15 + 0B111 it will get error because real part could be decimal, binary, hexa, oct but
# imag part must be decimal and it could not be binary, hexa or octal


# 5
"""
 bool data type:
 its complusry  True or Fales not true and false are applicable
"""
b= True
print(type(b))

# b  = true it will get error
a = 10
b = 20
c = a > b
print(c)

print(True + True)   # here True is 1 and False is 0 will get internally
print(True - False)
print(True * False)

# 6
""" string data type:
single and double quotes are not used for multiple line 
but triple quotes are used for comment
"""
s = 'Shiva'
print(type(s))
s= "Shiva"
print(type(s))
# in python there is no char data type
s = 'a'
print(type(s))
print(s)

Shiva = 'Shiva going to be "12 months in sept" so we will celebrate her birthday'
print(Shiva)

# Shiva = 'shiva is good 'good girl' and shhe wil be "good" ' we will get error int his senteence

Shiva = ''' shiva is 'good' and she will be "good" '''
print(Shiva)


# index
s = 'Shiva'
print(s[0])
print(s[1])
print(s[-1])
print(s[-3])
print(s[3])


#slice operator
a = 'abcdefghijklmnopqrstuvwxyz'
print(a[3:9])  # 3 to 8 return substring(slice) from begin index to end-1 index
print(a[:9]) # 0 to 8
print(a[3:]) # 3 to end
print(a[:]) # 0 to end
print(a[5:1]) # it will get empty

s = 'shiva'
output = s[0].upper() + s[1:]
print(output)

output = s[0:4] + s[-1].upper()
output = s[0:len(s)-1] + s[-1].upper()
print(output)
print(output)

output = s[0].upper() + s[1:len(s)-1] + s[-1].upper()
print(output)

# + operator
s = 'shiva' + 'patoliya'
print(s)

s= 'Shiva' + ' ' + 'Patoliya'
print(s)

# * multipliction operator will work for string and we can apply with one string and one int
s = 'Shiva' * 2
print(s)
s = 3 * 'Shiva'
print(s)

# s = 'Shiva' * 'Shiva' we can not multiply two string
# print(s)

print('#' * 10)
print('Shiva' * 1)
print('#' * 10)

# Type casting type conversion
# int() method
print(int(10.9908)) # float to int

# int(10+20j) we will get type error --> complex to int

print(int(True)) # bool to int

print(int('15')) # int to str
''' string internally contain integral value and base-10 we can not convert hexa, oct
bin string to int
'''
# print(int('0B111') it will get error
# print(int('10.5') it will get error because it is floating no

# float():
print(float(15))   # int to float
print(float(0B111))

# print(float(10+20j))  complex to float we will get error

print(float(True))  # bool to float
print(float(False))

# in string to float, string should be contain internally int value or float value
print(float('15'))
print(float('20.7'))
# print(float('0XFace') we will get error
# print(float('Shiva') we will get error

#complex
# this is only for real value

print(complex(10)) # int to complex
print(complex(0B111)) # int to complex
print(complex(10.5))  # float to complex
print(complex(True))  # bool to complex
print(complex(False))  # bool to complex
print(complex('10'))   # string to complex
print(complex('10.5')) # string to complex
# print(complex('0B111') # string should be contain int or float no

# this is only for real and imag value
print(complex(10,20))  # int to complex
print(complex(10.20, 20.5))  # float to complex
# print(complex('10', '20')  we can not pass both string value in real and imag
# print(complex(10, '20'))


# bool
print(bool(10))  # int to bool here 10 not 0 thats why we will get true otherwise we will get false
print(bool(0))
print(bool(-10))

print(bool(10.3))   # float to bool
print(bool(0.0))
print(bool(0.1))

print(bool(10)) # complex to bool
print(bool(0+0j))
print(bool(1 +0j))

print(bool('True'))  # string to bool
print(bool('False'))
print(bool('yes'))
print(bool('no'))
print(bool(''))

#str()

print(str(10)) # int to str
print(str(0B111)) # int to str
print(str(10.5)) # float to str
print(str(True)) # bool to str
print(str(False)) # bool to str
print(str(10+20j)) # complex to str

# 7
'''fundamental data types and immutability
mutable means can change
immutable means can not change
once, we create object we can not perform any changes in that object 
if we are trying to perform any changes, with those changes , a new object will be created 
'''
x = 10
print(id(x))
x = x + 1
print(id(x))
x= 10
y= x
print(id(x))
print(id(y))

y=y+1
print(x)
print(y)
print(id(y))
print(id(x))

a= 10
b=10
c=10
print(id(a))
print(id(b))
print(id(c))

# memory utilization and performance is good and object reausability concept not applicable
# only for complex

a = 100000.234
b = 100000.234

print(id(a))
print(id(b))
print(a is b)

a = True
b = True
print( a is b)

a= 'Shiva'
b = 'Shiva'
print(a is b)

''' voter registration application:
name:
Father name:
Mother Name:
Address:
'''
#list
'''Lists can contain millions of items, so Python provides an
efficient way to loop through all the items in a list. When
you set up a loop, Python pulls each item from the list one
at a time and stores it in a temporary variable, which you
provide a name for. This name should be the singular
version of the list name.
 The indented block of code makes up the body of the
loop, where you can work with each individual item. Any
lines that are not indented run after the loop is completed. '''
''' 
#List data type(collection related data type) and is mutable
#order preserved and duplicates are allowed and values should be in [], indexes and sliceing
# concept is available, growable in nature and mutable
'''
#looping through list

#printing all item in list
users = ['anu','mira','dia','nena','renuka','hiren']
for user in users:
    print(user)

#Printing a message for each item, and a separate message afterwards
for user in users:
     print('Welcome,' + user + '! ' )

print('Welcome, we are glad to see you all!')

#the range function
'''You can use the range() function to work with a set of
numbers efficiently. The range() function starts at 0 by
default, and stops one number below the number passed to
it. You can use the list() function to efficiently generate a
large list of numbers'''
#printing the number 0 to 10
for number in range(10):
    print(number)   #its printing too many

#pringing number from 1 to 10
for number1 in range(1,11):
    print(number1)

#Making a list of numbers from 1 to 101
numbers = list(range(1,101))
print(numbers)
users = ['hiren','shiva','renuka']
for user in users:
    print('welcome to ' + user + '!')
print('I really happy to see all users here!')

bikes = ['trek','redline','giant']
for bike in bikes:
    print(bike)

#adding item to list
squares = []
for x in range(1,12):
    squares.append(x**2)

print(squares)

squares1 = []
for x in range(1,12):
    print(x)

#list comprehnsion
'''You can use a loop to generate a list based on a range of
numbers or on another list. This is a common operation, so
Python offers a more efficient way to do it. List
comprehensions may look complicated at first; if so, use the
for loop approach until you're ready to start using
comprehensions.
 To write a comprehension, define an expression for the
values you want to store in the list. Then write a for loop to
generate input values needed to make the list.'''

squares2 = [x**2 for x in range(1,12)]
print(squares2)

names = ['kai', 'abe', 'ada', 'gus', 'zoe']

upper_names = []
for name in names:
    (upper_names.append(name.upper()))

print(upper_names)

#Using a comprehension to convert a list of names to upper case
names = ['kai', 'abe', 'ada', 'gus', 'zoe']
upper_names = [name.upper() for name in names]

print(upper_names)

#visulizing your code
'''When you're first learning about data structures such as
lists, it helps to visualize how Python is working with the
information in your program. pythontutor.com is a great tool
for seeing how Python keeps track of the information in a
list. Try running the following code on pythontutor.com, and
then run your own code.'''
dogs = []
dogs.append('whillie')
dogs.append('hootz')
dogs.append('peso')
dogs.append('goblin')

for dog in dogs:
    print('hello' + dog + '!')
print('I love these dogs!')

print("\nThese were my first two dogs:")
old_dogs = dogs[:2]

for old_dog in old_dogs:
    print(old_dog)

#deleting,removing,adding,slicing,indexing operation on list
del dogs[0]
dogs.remove('peso')
print(dogs)

l=[]
l.append(10)
l.append(20)
l.append(30)
l.append(40)
print(l)

l.remove(30)
print(l)

l.append(20)
print(l)

l[0] = 777
print(l)

bikes = ['trek','redline','giant']
print(bikes[0])
print(bikes[-1])

#mutable concept
list1 = [10,20,30,40]
print(list1)
print(id(list1))
list1[0] = 70
print(list1)
print(id(list1))

l1=[10,20,30,40]
l2 =l1
print(l1)
print(l2)

l1[0] = 7777
print(l1)
print(l2)

l2[1]= 888
print(l1)
print(l2)

#slicing list
l=[10,'Shiva',20,30,10]
print(type(l))
print(l)
print(l[0])
print(l[-1])
print(l[1:4])

#making list
users = ['val','bob','mia','ron','ned']
print(users)

#changing element
users[0]='valeri'
users[-2] = 'ronald'
print(users)

#adding elements to end of the list
users.append('amy')

#inserting element at particular position
users.insert(0,'Joe')
users.insert(3,'bea')
print(users)

#removing elements
del users[-1]
users.remove('mia')

#pop
'''If you want to work with an element that you're removing
from the list, you can "pop" the element. If you think of the
list as a stack of items, pop() takes an item off the top of the
stack. By default pop() returns the last element in the list,
but you can also pop elements from any position in the list.'''
print(users.pop())
print(users.pop(0))
print(users)

#list length
print(len(users))
leng = len(users)
print(leng)
print('we have '+str(leng)+' '+'users')

#sorting list
users.sort()
print(users)

#Sorting a list permanently in reverse alphabetical order
users.sort(reverse=True)
print(users)
users.sort(reverse=False)
print(users)

#reversing the order of list
users.reverse()
print(users)

#looping through list

#finding minimum value in list
ages = [12,34,45,34,22,36,12,30,28,26,20]
print(min(ages))
print(max(ages))
print(sum(ages))

#changing elements
l = ['hiren','nena','diza']
l[0] = 'Renuka'
print(l)

finishers=['renu','shiva','hiren','diya']
print(finishers[:2])

#copying list
copy_of_finishers = finishers[:]
print(copy_of_finishers)

#tuples:
tuple1 = (10,20,30,40)
print(tuple1)
'''
we can not do 
[0]= 7777
tuple1.append(20)
tuple1.remove(40)
'''

t = ()
print(type(t))
t = (10)
print(type(t))
t = (10,)
print(type(t))

#difference between tuple and list
#list is mutatble, can defined in  [], more memory and performance is less
#tuple is immutable, can defined in (), less memory and performance is high


#set data types
#duplicates are not allowed and order is not required, inexing and slicing is not allowed and heterogenous
# boject are allowed, and we can add and remove object so its mutable and growable
s = {10,20,30,40}
print(type(s))
s={10,20,10,'durga',30,40}
print(s)

#print(s[0])
#print(s[0:4])

s={10,20,30,40,50}
s.add(60)
print(s)
s.remove(50)
print(s)

#in append method elements always add at last but in add method there is not garuntee to where elements is add
s ={}
print(type(s))
s = set()
print(s)

#frozen set
s = {10,20,30,40,50}
fs = frozenset(s)
print(type(fs))
#forzen set is now immutable object and we can not change it

#fs.add(20)
#fs.remove(30)
frozenset1 = frozenset({10,20,30,40,50})
print(frozenset1)
print(type(frozenset1))

#dictionary
#duplicates are not allowed in key but we can take as value as duplicates but if you use
#order is not applicable,mutable,slicing not applicable
d={100:'Shiva',200:'hiren',300:'renuka'}
print(type(d))

d={}
d[100] = 'Jaya'
d[200] = 'Shiva'
d[300] = 'Hiren'
d[400] = 'Renuka'
print(d)
d[100] = 'Purva'
print(d)

#range data types, slicing is applicable , its immutable we can not change element, order is applicable
# its provide indexing ,
'''r=range(10)
print(r)
print(type(r))
for x in r:
    print(x)
    '''

'''r1=range(1,10)
for x in r1:
    print(x)
'''
r=range(1,21,1)
for x in r:
    print(r)

r=range(1,21,2)
for x in r:
    print(r)

r=range(1,21,3)
for x in r:
    print(r)

r=range(20,1,-5)
for x in r:
    print(x)

r = range(10,21)
for x in r:
    print(x)
print(r[0])
print(r[-1])
print(r[1:5])

r1 = range(10,20)
for x in r1:
    print(r1[1:5])

#r[1] = 1000 we can not change element because its immutable

#bytes data type:
#values only from 0 to 255,immutable,
l=[10,20,30,40,50,256]
b=bytes(l)
print(type(b))
for x in b:
    print(x)
print(b[7])

#b[0] = 77 we will get type error becasue we can not get it

#bytearray:
# bityearray is mutable ,
l=[10,20,30,40]
b = bytearray(l)
print(type(b))
print(b[0])
print(b[-1])
#if you add 256 you will get error like range should be in
b[0]=77
for x in b:
    print(x)

'''
int = to represesnt whole number(a=10), immutable,no Insertion order preserved,no indexing ans slicing, no duplicates
float = to represent floating value(a = 10.3), immutable,no Insertion order preserved,no indexing ans slicing, no duplicates
complex = to represent complex number(a = 1-+20j),immutable,no Insertion order preserved,no indexing ans slicing, no duplicates
boolean = to represent logical value only  a=true, b =False, immutable,no Insertion order preserved,no indexing ans slicing, no duplicates
string = to represent a sequence of character, immutable,no Insertion order preserved,indexing and slicing, no duplicates
list = an ordered collection of object, mutable,insertion order preserved, indexing and slicing and duplicates are allowed
tuple =read only version of list, immutable,insertion order preserved, indexing and slicing and duplicates are allowed
set = an unordered collection of unique objects, mutable,no insertion ordered preserved,no indexing,slicing and duplicates
frozenset = read only version of set, immutable, no insertion ordered preserved, no indexing, slicing and duplicates 
dict = to represenetd key value pair,mutable, no insertion ordered preserved,no indexing and slicing but key no duplicates but vlaue
byte= to group of byte value,immutable,insertion ordered preserved,indexing, slcing and duplicates are allowed
bytearray = a group of bytevalue, mutable,insertion ordered preserved ,indexing, slicing and duplicates are allowed
range = sequence of value , immutable, insertion ordered preserved,indexing and slicing apllicable but no duplictes

'''

#none data type:
def f1():
    return 10

x = f1()
print(x)

def f1():
    print('hello')

x = f1()
print(x)

a=None
print(a)
print(id(a))
print(type(a))

a= None
b= None
c= None
def f1():
    pass
d= f1()
print(id(a))
print(id(b))
print(id(c))

print(a,b,c,d)


#Escape character:
'''
\n =new line
\t = horizontal tab
\ = back slash
\r = carriage return
\b = back space
\f = form feed
\' = single quote
\'' = double quote
\\ = double slash
'''
print('RenukaPatoliya')
print('Renuka\tPatoliya')
print('Shiva\nPatoliya')
print('This shiva\'s House') #back slash


#comments:
# symbol used for single line comments
''' this symbol used for multiline comments'''

#constants in python:
'''constant is not applicable in python like in java there is final keyword to used for constant'''

