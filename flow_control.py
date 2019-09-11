#Indentation
# if condtition:
#     statement 1
#     statement 2
#     statement 3
#     staement 4
#if statement:
if 10<20:
    print('10 is less then 20')
print('end the program')

name = input('enter name')
if name == 'Renuka':
    print('Hello Renuka, good Evening ')
print('How are you!')

#if-else statement:
name = input('enter your name here:')
if name == 'Shiva':
    print("hello shiva how are you!")
else:
    print("hello Guest how are you?")
print("hello good morning!")

#if-elif-else statement:
brand = input('enter your fav brand:')
if brand == 'kf':
    print('this brand is for kids')
elif brand == 'ko':
    print('this is too light brand')
elif brand == 'fo':
    print('buy one get one free')
else:
    print('other brand is not recommended')

#write programe to find biggest of 2 given no
a = int(input('enter first no:'))
b= int(input('enter secong no:'))
if a>b:
    print('a is biggest no')
else:
    print('b is biggest no')

#find smallest no
a = int(input('enter first no:'))
b= int(input('enter secong no:'))
if a<b:
    print('a is smallest no')
else:
    print('b is smallest no')

#find biggest no from three input values
a=int(input('enter first no'))
b=int(input('enter second no'))
c=int(input('enter third no'))
if a>b and a>c:
    print('a is biggest no')
elif b>c:
    print('b is biggest no')
else:
    print('c is biggest no')

#find smallest no from three input values
a=int(input('enter first no'))
b=int(input('enter second no'))
c=int(input('enter third no'))
if a<b and a<c:
    print('a is smallest no')
elif b<c:
    print('b is smallest no')
else:
    print('c is smallest no')

#given no is between 1 to 100 or not?
n= int(input('write any no here'))
if n>=1 and n<=100:
    print('the {} is between 1 and 100'.format(n))
else:
    print('the {} is not between 1 and 100'.format(n))

#enter any digit no and get output in word

n=int(input('enter any no here from 1 to 10'))
if n==0:
    print('zero')
elif n==1:
    print('one')
elif n==2:
    print('two')
elif n==3:
    print('three')
elif n==4:
    print('four')
elif n==5:
    print('five')
elif n==6:
    print('six')
elif n==7:
    print('seven')
elif n==8:
    print('eight')
elif n==9:
    print('nine')
elif n==10:
    print('ten')
else:
    print('please enter the value between 0 to 10')

#another way
n=int(input('enter the digit 0 to 9 here:'))
words = ['zero','one','two','three','four','five','six','seven','eight','nine']
print(words[n])

#convert digit 0 to 100 in words
word_upto_19 = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twel','thirtee'
                ,'fourteen','fifteen','sixteen','seventeen','eighteen','ninteen']
word_upto_99 =['','','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninty']

n = int(input('please enter here 1 to 100 digit'))
output =''
if n==0:
    print('zero')
elif n<=19:
    print(word_upto_19[n])
elif n<=99:
    print(word_upto_99[n//10] + ' ' + word_upto_19[n%10])
else:
    print('please enter betweeen 1 to 100')

#Iterative statement:
#for loop and while loop:
s='Shiva Patoliya'
for x in s:
    print(x)

s='Shiva Patoliya'
i=0
for x in s:
    print('The character present at {} index:{}'.format(i,x))
    i=i+1

s=(input('please enter here any string'))
i=0
for x in s:
    print('The character present at {} index:{}'.format(i,x))
    i=i+1

#range
for x in range(10):
    print('Hello welcome to python')

for x in range(1,11):
    print(x)

#to display odd no from 0 to 20
for x in range(21):
    if x%2!=0:
        print(x)

#another way
for x in range(1,21,2):
    print(x)

#to display no from 10 to 1 in decending order:
for x in range(10,0,-1):
    print(x)

#to print the sum of number in the given list:
# list = eval(input('enter any list no here:'))
# sum =0
# for x in list:
#     sum = sum + x
#     print('sum of list:',sum)

list = int(input('please enter here any list value'))
sum = 0
for x in list:
    sum = sum + int(x)
    print('sum of list',sum)

list = eval(input('please enter here any list value'))
print(sum(list))

#while condition
i=1
while i<=10:
    print('hello welcome to while loop')
    i= i+1

i=1
while i<=10:
    print(i)
    i=i+1

#to print number from 1to 20 which are divided by 3
x=1
while x<=20:
    if x%3==0:
        print(x)
    x=x+1

#sum of first n number:
n=int(input('please enter here any no:'))
sum=0
i =1
while i<=n:
    sum=sum+i
    i=i+1
print('sum of first n:',sum)

name = ''
while name !='Shiva':
    name = input('enter your fav actress here:')
print('thank you for your confirmation!')

#infinite loop:
i=1
while True:
    print('hello pyhton',i)
    i=i+1

#nested loop:
for i in range(3): #i=0,1,2
    for j in range(2): #j=0,1
        print('hello')

for i in range(3):
    for j in range(2):
        print('i={},j={}'.format(i,j))

if True:
    print('hello my name is renuka')
if 2>1:
    print('2 is bigger than 1 and it is True:')

#The “else” statement will be executed if the “if” expression is false.
if 1>2:
    print('this is false')
else:
    print('this is not true:')

if 1 > 2:
 print("1 is greater than 2")
elif 2 > 1:
 print("1 is not greater than 2")
else:
 print("1 is equal to 2")

 num=1
 while num<=10:
     print(num)
     num +=1

loop_condition = True
while loop_condition:
    print("Loop Condition keeps: %s" %(loop_condition))
    loop_condition = False

Renuka=True
while Renuka:
    print('this is True and it will printing:')
    Renuka=False

#list is collection
