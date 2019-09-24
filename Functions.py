#functions
#without functions
a=10
b=10
print('sum of a and b',a+b)
print('difference between a and b',a-b)
print('the producto of a and b',a*b)
a=100
b=300
print('sum of a and b',a+b)
print('difference between a and b',a-b)
print('the producto of a and b',a*b)

#with functions
def calculation(a,b):
    print('sum of a and b', a + b)
    print('difference between a and b', a - b)
    print('the producto of a and b', a * b)
calculation(10,20)
calculation(100,300)

#with another ways
a=int(input('enter a value here'))
b=int(input('enter b value here'))
print('sum of a and b',a+b)
print('difference between a and b',a-b)
print('the producto of a and b',a*b)

#types of fuctions:
#1-built in function/predefined function like id(),type(),print(),eval(),input() etc
#2-userdefined or customized functions
def wish():
    print('hello friends good evening')
wish()
wish()
wish()

#functions parameters
def wish(name):
    print('hello',name ,'welcome to india')
wish('Renuka')
wish(input('please type your name here:'))

def squareit(num):
    sq=num*num
    print('the square value of {} is {}'.format(num,sq))
squareit(3)
squareit(16)

#return statement:
def add(a,b):
    sum=a+b
    return sum
add(10,20)
result=add(200,400)
print('sum of a and b',result)
print('sum of a and b',add(40,50))

def f1():
    print('hello')
x=f1()
print('here return value will be printed none',x)
print(x)

def factorial(num):
    result=1
    while num>=1:
        result=result*num
        num=num-1
    return result
print('factorial no here',factorial(3))
print(factorial(4))
print(factorial(5))

for i in range(1,6):
    print('the factorial of ',i,'is ',factorial(i))

#returning multiple values from a function
def sum_sub(a,b):
    sum=a+b
    sub=a-b
    return sum,sub
x,y=sum_sub(10,20)
print('sum of x',x)
print('sum of y',y)

def cal(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
t=cal(10,30)
print(type(t))
print(t)
for x in t:
    print(x)

#types of arguments:positional arguments,keyword arguments,default argument,variable length arguments
#positional argument
def sub(a,b):
    print(a-b)
sub(100,200)
#here is order is mandatory means a must be 100 and b must be 200
sub(200,100)


#keyword argument:
def sub(a,b):   #here a nd b is formal paramters
    print(a-b)
sub(100,300)    #here 100 and 300 are actual arguments
sub(a=300,b=500)
sub(b=400,a=200)
sub(100,b=900) #here we can not use first keyword argument ,first should be positional argument
sub(200,a=599)

#default argument:
def wish(name):
    print('hello',name,'welcome')
wish('Renuka')
# wish() we will get error

def wish(name='Guest'):
    print('hello',name,'welcom')
wish()
wish('Hiren')
wish('Shiva')

def wish(name,msg):
    pass
def wish(name='Geuest',msg='Hello good morning'):
    print('hello',name,msg)
wish()
wish('Renuka')
wish('Shiva','Hello how are you ')

def wish(name,msg='Hello how are you'):
    print('hello',name,wish())
# wish() here we will get error because name is not set as default
wish('Renuka')
wish('Hiren','How are you')


'''
def wish(name='Guest',msg):
    pass
#this syntax is invalid
'''

#variable lenght argument:


