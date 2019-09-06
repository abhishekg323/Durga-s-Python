#Arithmetica operator
'''
/ = normal division
// = floor division

'''
a=10
b= 2
print(a+b)
print(a-b)
print(a*b)
print(a%b) # it will give reminder ans
print(10/2) #normal division operator
print(a/b)
print(10/3) # floor division operator and its meant for integral and floating value
print(10//2)
print(10//3)
print(10.0/2)
print(10/3)
print(10.0/3)
print(10//3)
print(10.0//3)

print(20/2)
print(20.5/2)
print(20//2)
print(20.0/2)
print(30//2)

print(10**2) # here ** is exponetial
print(3**3)

print('Shiva'+'Patoliya')
print('Shiva'+ ' ' + 'Patoliya')
print('Hiren' + '10')
print('Renuka' + str(10))

print('Renuka'*3)
print(3*'Hiren')
#print('Renuka' * 'Jaya')  we will get error
# because one argument must be string and one int
 # print('Jaya' * '3')

print('Meera' * int('3'))

# print(10/0) we will get modulo by zero error
# print(x/0)
#print(x.0/0)

print('Hiren' * True)
print('Anu'* False)

#Relational operators:
a=10
b=20
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

s1 = 'a'
s2 = 'b'
print(ord(s1))
print(ord(s2))
print(chr(97))
print(ord('A'))

s1 = 'Shiva'
s2 = 'Nena'
print(s1>s2)
print(s1<s2)
print(s1>=s2)
print(s1<=s2)

s1 = 'Diza'
s2 = 'Diza'
print(s1>s2)
print(s1<s2)
print(s1>=s2)
print(s1<=s2)

s1 = 'Shiva'
s2 = 'shiva'
print(s1>s2)
print(s1<s2)
print(s1>=s2)
print(s1<=s2)

print(True > False)
print(True < False)
print(True >= False)
print(True <= False)

a= 10
b = 20
if a >b:
    print('a is greater than b')
else:
    print('a is less than b')

print(10<20)
print(10<20<30)
print(10<20<30<40)
print(10<20<30>40>50)  #if any one statement will be false than result will be false

#equality operators:
print(10==20)
print(10!=20)
print(1==True)
print(10==10.0)
print('Shiva' == 'Shiva')
print(10 == 'Hiren')
print(10=='10')
print(10==20==30==40)
print(10==10==10==10)

# difference between == operator and 'is' operator
l1 = [10,20,30,40]
l2 = [10,20,30,40]
print(id(l1))
print(id(l2))

print(l1==l1)
print(l1 is l2)

l3 = l1
print(l1 is l3)
print(l1==l3)

#logical operators for boolean type:and, or, not(complement)

print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or False)
print(True or True)
print(False or False)
print(False or True)

print(not True)
print(not False)

'''username = input('enter username:')
password = input('enter password:')
if username== 'Shiva' and password== 'Patoliya':
    print('this is valid user')
else:
    print('this is invalid user')
'''
#logical operators for non-boolean type:
'''
x and y
if x evaluates to False, then result is x
if x evaluates to True, then result is y
if x is 0 then its mean x is false and result will be 0
if x is none zero thats means x is True and result is y
'''
print(10 and 20 )
print( 0 and 20 )

print('Shiva' and 'Patoliya') # here Shiva is non-empty string so its True so result is Patoliya
print('' and 'Hiren')  # here first string is empty

'''
x or y
if x is True then result is x
if x is False then result is y
'''
print(10 or 20)
print(0 or 20)
print([] or 'Shiva')
print('Hiren' or 'Renuka')

#not for non-boolean type the result is in boolean
print(not 'durga')
print(not '')
print(not 0)
print(not 10)

#bitwise operators: only for int and boolean data type
'''
& --> bitwise and(if both bits are '1' then result is 1 otherwise '0')
| --> bitwise or(if atleast one bit is '1' then result is 1 otherwise '0')
^ --> bitwise x-or(if both bits are different then result is 1 otherwise '0')
~ --> bitwise complement operator
<< --> bitwise left-shift operator
>> --> bitwise right-shift operator
'''
#print(10.20 & 20.30) we will get type error
#print('durga & 'durga')

print(10 & 20)
print(4&5)
print(4|5)
print(4^5)

#bitwise complement operator:
print(~4)
'''
The most significant bits act as sign bit
0--> +ve number
1--> -ve number
+ve number will be directly represented directly in the memory
-ve number will be represented in 2's complement form
1st complement => 0-->1
               => 1-->0
2nd complement 1's complement + 1
'''
print(~5)
print(~-4)

#shift operator: <<, >>
print(10<<2) #this is left shift operator
print(10>>2) #this is right shift operator

print(True & False)
print(True & True)
print(True| False)
print(True | True)
print(True^False)
print(True^True)
print(~True)
print(~False)
print(~1)
print(True<<2)
print(False<<2)
print(True>>2)
print(False>>2)

#Assignment operator:
#in python increment and decrement operator are not applicable
x= 10
print(++x)
print(+++x)
print(-x)
print(--x)

x= 30
x+= 5
print(x)
x-=5
print(x)
x*=5
print(x)
x/=5
print(x)
x%=5
print(x)
x//=5
print(x)
x**=5
print(x)
x&=5
print(x)
x|=5
print(x)
x^=5
print(x)
x>>=5
print(x)
x<<=5
print(x)

#ternary operator:
#here is three agrument in one condition so
a=10
b=20
c=30 if a>b else 40
print(c)

'''
#read two int value from keyboard and print min value
a= int(input('enter first value here:'))
b = int(input('enter secong value here:'))
min = a if a<b else b
print('minimum value is:', min)
'''

'''#Nesting of ternary operator:
a=int(input('enter first number:'))
b=int(input('enter second number:'))
c=int(input('enter third number'))
min = a if a<b and a<c else b if b<c else c
#min = a if a<b<c else b if b<c else c try this one is but it will not give min values just try it and run it
print('minimum value is:',min)

max =a if a>b and a>c else b if b>c else c
print('maximum value:', max)
'''

a = int(input('please enter first value:'))
b= int(input('please enter second value:'))

result = "both numbers are equal" if a==b else "a is smaller than b" if a<b else "a is Bigger than b"
print('here is result of:', result)


#special operators:
#