#break statement:
#if break statement can not possible without for or while loop
for i in range(10):
    if i==7:
        print('processing is enough, break loop execution')
        break
    print(i)
print('out side of loop')

cart =[10,20,30,600,40,50]
for item in cart:
    if item>500:
        print('iteam is more than 500,so its reqired insurance,we can not go further')
        break
    print('processing item',item)

# x=10
# if x>40:
#     print('we are stopping program execution')
#     break
# print('hello')

#continue statement:
for i in range(10):
    if i%2==0:
        print(i)
        break
    print('hello')

#in continue:
for i in range(10):
    if i%2==0:
        continue
    print(i)

for i in range(10):
    if i%2!=0:
        continue
    print(i)

cart = [10,20,30,40,503,60,600]
for item in cart:
    if item>500:
        print('please skipped this item because its required insurance')
        continue
    print('processing item',item)

l=[10,20,0,40,30,50]
for x in l:
    print('100/{}={}'.format(x,100/x))

l=[10,20,0,40,30,50]
for x in l:
    if x==0:
        print('how it it possible divided by zero')
        continue
    print('100/{}={}'.format(x,100/x))

#here, we will get error because without for or while loop we can not use continue or break statements
# x=10
# if x>40:
#     print('hello')
#     continue
# print('hi')

#break and continue in loop
for i in range(3):
    for j in range(3):
        if i==j:
            break
        print(i,j)

for i in range(3):
    for j in range(3):
        if i==j:
            continue
        print(i,j)

#loops with else block:
cart = [10,20,30,40,50]
for item in cart:
    if item>500:
        print('we can not process this item because it required insurance')
        break
    print('processing iteam in progress',item)
else:
    print('congratualtions your all item succeessfully process')

#break
cart = [10,20,30,40,50,600]
for item in cart:
    if item>500:
        print('we can not process this item because it required insurance')
        break
    print('processing iteam in progress',item)
else:
    print('congratualtions your all item succeessfully process')

#break
cart = [10,20,30,40,50,600,50,60]
for item in cart:
    if item>500:
        print('we can not process this item because it required insurance')
        break
    print('processing iteam in progress',item)
else:
    print('congratualtions your all item succeessfully process')

#continue
cart = [10,20,30,40,50,600,50,60]
for item in cart:
    if item>500:
        print('we can not process this item because it required insurance')
        continue
    print('processing iteam in progress',item)
else:
    print('congratualtions your all item succeessfully process')

#pass statement:
def f1():
    pass

#if we do not do pass here then we will get error

class A:
    pass
class B:
    pass
class C:
    pass

#if  we do not do pass here then we will get error here
x=10
if x<100:
    print('success')
else:
    pass

#if you do not want to implement now else then you can say pass
#if you do not do implement and do not write pass then we will get error
from abc import *
class Loan(ABC):
    def getInterestRate(self):
        pass

class Home(Loan):
    def getInterestRate(self):
        return 8
class Vehicle(Loan):
    def getInterestRate(self):
        return 10

h=Home()
print(h.getInterestRate())

v=Vehicle()
print(v.getInterestRate())

#del statement:
x = 10
print(x)
del x
print(x)

s1='Shiva'
s2=s1
s3=s1
del s1
print(s2)
print(s3)
del s2
del s3

#del vs immutable object
s = 'Shiva'
del s

s='Renuka'
del s[0] #we will get error becaaseu del is used for delet object or reference but not for element

#list
l =[10,20,30,40]
print(l)
del l
print(l)

t =(10,30,40)
print(t)
del t

#del vs None
x=10
del x
print(x) #here we will get error

x=10
x=None
print(x)

#prime number introduction
#given number is prime or not?

n= int(input('enter here any number'))
if n<=1:
    print('It is not Prime Number')
else:
    is_prime=Trueg
    for i in range(2,n):
        if n%i==0:
            is_prime =False
            break
    if is_prime==True:
        print('It is prime number')
    else:
        print('It is not prime number')

#generate prime number which are less than or equal to given number:
n= int(input('enter here any number'))
n1=2
while n1<=n:
    #this code is to check whether n1 is prime or not
    is_prime=True
    for i in range(2,n1//2+1):
        if n1%i==0:
            is_prime=False
            break
    if is_prime==True:
        print(n1)
    n1=n1+1

#generate first prime number here:
n= int(input('enter here any no:'))
count=0
n1=2
while True:
    is_prime=True
    for i in range(2,n1//2+1):
        if n1%i==0:
            is_prime=False
            break
    if is_prime==True:
        print(n1)
        count=count+1
    if count==n:
        break



