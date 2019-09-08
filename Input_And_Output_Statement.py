#raw input() and input()
# this applicable only in 2.x version but in 3.X there is only one input()
x= raw_input('type any int value')
print(type(x))  #it will give string type whatever you typed

y = int(x)
print(type(y))
print(type(x))

x = input('type any thing here')
print(type(x))     #it will give type depend on what you typed lets say you type int value then will int

#but in python 3.x there is not any raw-input function but there is only input() and its
#works similar raw_input()

x= input('enter first no:')
y= input('enter second no:')
i= int(x)
j= int(y)
print('sum of :', i+j)

x= int(input('enter first no:'))
y= int(input('enter second no:'))
print('sum of:', x+y)

print('sum of :', int(input('enter first no:')) + int(input('enter second no:')))

#to write a program to read employee data from the keyboard
eno = int(input('enter emp no:'))
ename=input('enter empname: ')
esal = float(input('enter emp sal:'))
eadr = input('enter emp address:')
married = bool(input('emp married?[True/False]:'))
#married = eval(input('is employee marrried[True/False]:'))
print('please confirm data you provided')
print('Employeed No:',eno)
print('Employee Name:', ename)
print('Employee sal:',esal)
print('Employee address:', eadr)
print('Employee married:', married)

#reading multiple value from keyboard in single line
a,b=[int(x) for x in input('enter two value here:').split()]
print('sum of:', a+b)

s = input('enter two value here:')
l = s.split()
print(l)
l1 = [int(x) for x in l]
print(l1)
a,b = l1
print(a)
print(b)
print('sum of two values:', a+b)

a,b=[int(x) for x in input('enter two value here:').split(',')]
print('sum of:', a+b)

#write a program to read 3 float values from keyboard with , seperation and print the sum
a,b,c=[float(x) for x in input('enter three float value with , seperation:').split(',')]
print('sum of :', a+b+c)

#eval() function:
#alternative to typecasting is eval() functions
x= input('enter the input value here:')
print(type(x))
x= eval(input('enter here any int,bool,string and float value'))
print(type(x))
x= eval('10+20+39')
print(x)

#command line arguments:
#argv is list
from sys import argv
print(argv[0])

#write program to print command line argument one by one:
from sys import argv
print('the no of cmd line argument:',len(argv))
print('the limit of cm line  argument:', argv)
print('the cmd line argument one by one:')
for x in argv:
    print(x)

from sys import argv
#py test.py 10 20 30 40 50

args = argv[1:]
sum =0
for x in args:
    sum = sum+int(x)
print('sum:',sum)

#when we are using command line argument
#File merger application
f1 = open('file1.txt')
f2= open('file2.txt')
f3= open('output.txt','w')
for x in f1:
    f3.write(x)
for x in f2:
    f3.write(x)

#by command line argument:
f1 = open(argv[1])
f2= open(argv[2])
f3 =open(argv[3],'w')
for x in f1:
    f3.write(x)
for x in f2:
    f2.write()
# py.test.py a.txt b.txt c.txt
# py.test.py x.txt y.txt z.txt

#case-1
from sys import argv
print(argv[1])
#pass py test.py sunny leone
#pass py test.py "sunny leone"
# we should used complosary '' '' here ' ' will not work

#case-2
from sys import argv
print(argv[10] + argv[20])
print(int(argv[10]) + int(argv[20]))
#pass py test.py 10 20

#case-2
from sys import argv
print(argv[100])
#pass py test.py 10 20
# we will get error becaseu it is out of index means Index Error

#output Statement:
#print()
print('renuka ')
print()
print('hiren')

print('renuka\nhiren')
print('renuka\t hiren')
print('renuka' + 'hiren')
print(10*'renuka')

a,b,c = 10,20,30
print('values are :',a,b,c)

#sep attribute
a,b,c,d = 10,20,30,40
print(a,b,c,d)
print(a,b,c,d,sep=':')
print(a,b,c,d,sep='--')

#end attributes
print('hello')
print('durga')
print('soft')

print('hello',end='')
print('durga',end='')
print('soft')

print('hello',end='::')
print('durga',end='***')
print('soft')

print(10,20,30,sep=':',end='***')
print(10,20,30,sep=':')
print(70,80,sep='**',end='$$$')
print(90,100)

print('durga '+'soft')
print('durga','soft')

#print(object) and with replacement operator
l=[10,20,30,40,50]
print(l)
t= (10,20,30,40,50)
print(t)

name = 'Renuka'
salary = 10000
bf = 'hiren'
print('hello {},your salary is {} and your friend {} is waiting'.format(name,salary,bf))
print('hello {0},your salary is {1} and your friend {2} is waiting'.format(name,salary,bf))
print('hello {2},your salary is {1} and your friend {0} is waiting'.format(name,salary,bf))
print('hello {n},your salary is {s} and your friend {f} is waiting'.format(n=name,s=salary,f=bf))

a,b,c,d = 10,20,30,40
print('a={},b={},c={},d={}'.format(a,b,c,d))

#print with formatted string
# %i --> siged decimal value
# %d--> sigen decimal value
# %f--> float value
# %s --> string
a= 10
print('a value:%i',%a)
a=10
b=20
c=30
print('a=%d,b=%d,c=%d',%(a,b,c))

name = 'renuka'
marks= [10,20,40]
print('Hello %s, your list of mark:%s' %(name,marks))

price=70.56789
print('price value={}'.format(price))
print('price value=%f' %price)
print('price value=%.2f' %price)










