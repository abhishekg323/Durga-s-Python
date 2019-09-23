#List Data Structure:
#list allowed duplicates,
# its collection data type,
# insertion order preserved,
# heterogenous objects are allowed,
# list is dynamical,
# list is mutable becase add or replace elements in list,
# its declared in []

l=[]
l.append('Shiva')
l.append('Hiren')
l.append('16th sep')
print(l)
l[0]='Renuka'
print(l)

#empy list object
l=[]
print(type(l))

#dynamic list
l=eval(input('type here list:'))
print(type(l))
print(l)

#by usding list()
l=list('Shiva')
print(l)

l=list(range(0,10,2))
print(l)

s='Learning Python Is Very Eeasy'
l=s.split()
print(l)

#access elements of list
#by using index and by using slice operator
l=[10,20,30,40]
print(l[0])
print(l[-1])
print(l[len(l)-1])
#print(l[100] we will get index error

l=[10,20,30,40,40,50,60,607,60,70,80]
print(l[2:7])
print(l[2:7:2])
print(l[4::2])
print(l[8:2:-2])
print(l[4:100])
print(l[4:0:2])
print(l[::-1])
print(l[::1])

#traversing elements of all list
#by using while loop
l=[0,1,3,5,6,6,7,8,9,90]
i=0
while i<len(l):
    print(l[i])
    i=i+1

#by using for loop
for x in l:
    print(x)

for x in l:
    if x%2==0:
        print(x)

#print element by index wise

l=[10,20,30,40,50,60,70]
i=0
while i<len(l):
    print('positive {} and negetive {} index of  {}'.format(i,i-len(l),l[i]))
    i=i+1

#mathemeticals operators of list:
#concatenation operator(+)
#repeatation operator(*)
l1=[10,20,30,40]
l2=[20,40,60,80]
l3=l1+l2
print(l3)
# l2=l1+40  we will get erorr
l4=l1 + [40]
print(l4)
# l5=l1 + (10,20,30) we can not concatenate list with tuple

#repetation
l1=[10,20]
l2=l1 * 2
print(l2)
l2=2*l2
print(l2)

l1=[10,20]
l2=[30,40]
l3=l1+l2
l4=l3*3
print(l4)

#equality operator for list
# == ,!=

l1=['Dog','Rat','Cat']
l2=['Dog','Rat','Cat']
l3=['DOG','RAT','CAT']
l4=['Cat','Rat','Cat']
print(l1==l2)
print(l2==l3)
print(l3==l4)
print(l1!=l4)

#Relational Operators
#<,<=,>,>=
l1=[10,20]
l2=[50,60,30,40]
print(l1<l2)
print(l1<=l2)
print(l1>l2)
print(l2>=l2)

l1=['Rabha','Ramya']
l2=['Rama','Sunnuy']
print(l1<l2)

#membership operator
l1=[10,20,30,40,50]
print(10 in l1)
print(50 not in l1)
print(70 in l1)

#important methods and functions for list:len(),count() and index()
l=[10,20,30,40,40,50,60,60,60,70,70,8,8,8,20]
print(len(l))
print(l.count(50))
print(l.count(70))
print(l.count(20))
print(l.count(60))
print(l.count(90))
print(l.index(10))
print(l.index(50))

l=[1,2,3,4,4,4,5,5,6,6]
for x in l:
    print('{} present at {} index'.format(x,l.index(x)))

l=[1,2,3,4,5,6,6,6,7,7,7,7,8,7,5]
x=input('please enter here string')
if x in l:
    print('{} present at {}'.format(x,l.index(x)))
else:
    print(x,'is not available in index')

#manipulating element of list:
l=[]
l.append(10)
l.append(20)
l.append(30)
l.append(40)
print(l)

l=[]
for x in range(1,101):
    if x%10==0:
        l.append(x)
print(l)

#insert
#l.insert(index,element)
l=[10,20,30,40]
l.insert(1,7777)
print(l)
l.insert(20,8888)
print(l)
l.insert(-30,999)
print(l)

#extend
order1=['chicken','mitton','fish']
order2=['KF','KO','RC']
order1.extend(order2)
print(order1)

l1=[10,20,30]
l2=[30,40]
l1.append(l2)
print(l1)
print(len(l1))

l1=[10,20,30]
l2=[40,50]
l1.extend(l2)
print(l1)
print(len(l1))

l1=[10,20,30]
l2=['ABC']
l1.append(l2)
print(l1)
print(len(l1))

l1=[10,20,30]
l2=['ABC']
l1.extend(l2)
print(l1)
print(len(l1))

l1=[10,20,30]
l1.extend('ABC')
print(l1)
print(len(l1))

#remove
l=[10,20,30,40,40,30]
l.remove(20)
print(l)
l.remove(40)
print(l)
# l.remove(50) here we will get value error

l=[1,2,3,4,5,6]
x=int(input('please enter here any no'))
print('before removal:',l)
if x in l:
    l.remove(x)
    print('after removal:',l)
else:
    print('this elements are not available in list')

#how to remove all occurences
l=[1,1,1,1,1,3,3,3,3,4,4,4,2,2,]
x=int(input('enter elements to removal:'))
print('before removal',l)
while True:
    if x in l:
        l.remove(x)
    else:
        break
print('after removal',l)

#pop() and clear()
l=[10,20,30]
print(l.pop())
print(l)
l.pop()
print(l)
l.pop()
print(l)
#l.pop() we will get index error
#l.pop(index)
l=[10,20,30,40]
print(l.pop(1))
print(l)

#clear()
l=[10,20,30,40]
print(l)
l.clear()
print(l)

#in list we can increase the size of list by using append, extend and insert methoda
#also decrease the size of list by using pop,remove and clear methods

#ordering elements of list:
l=[10,20,30,40,50]
print('before reversal',l)
l.reverse()
print('after reversal',l)

l=[10,20,30,40,50,60]
r=reversed(l)
print(r)
l1=list(r)
print(l)
print(l1)

s='Shiva'
# s.reverse we can not apply here
r=reversed(s)
for x in r:
    print(x)
l=list(r)
print(l)

#sort() and sorted()
l=[0,5,4,3,5,67,89,20]
print('before sorting',l)
l.sort()
print('after sorted',l)

l=['banana','cat','apple']
print('before sorting',l)
l.sort()
print('after sorting',l)

l=[1,0,80,60,4,5,6,70]
print('before reveese sorting',l)
l.sort(reverse=True)
print('After reverse sorting',l)

# in short() all elements should be heterogenous
#sorted is in build python function and can apply anywhere else
#but sort() is not in built funcition and its applicable only for list
l1=[10,20,30,40]
print(l1)
l2=sorted(l1)
print(l2)

#aliasing and cloning of list object:
l1=[10,20,30,40]
l2=l1
l[1]=777
print(l1)
print(l2)
print(id(l1))
print(id(l2))

#cloning
l1=[10,20,30,40]
l2=l1[::]   # or l2=l1.copy()
print(l1)
print(l2)
print(id(l1))
print(id(l2))

l1[1]=777
print('l1:',l1)
print('l2:',l2)

#nested lists:
l=[10,20,30,[40,50]]
print(l[0])
print(l[1])
print(l[2])
print(l[3][0])
print(l[3][1])

l=[[10,20,30],[40,50,60],[70,80,90]]
print(l)
print('print element in row type')
for x in l:
    print(x)
print('print element in matrix type')
for x in l:
    for y in x:
        print(y)   # print(y,end=' ')


#list comprehnsion:
l=[]
for i in range(1,11):
    l.append(i)
print(l)

l=[x for x in range(1,11)]
print(l)

l=[x*x for x in range(1,101)]
print(x)

l=[2**x for x in range(1,6)]
print(l)

l=[x for x in range(1,101) if x%10==0]
print(l)

l1=[10,20,30,40]
l2=[30,40,50,60]
l=[x for x in l1 if x not in l2]
print(l)

l4=[x for x in l1 if x in l2]
print(l4)

l=['Shiva','Hiren','Renuka']
l1=[word[0] for word in l]
print(l1)
l2=[word[1] for word in l]
print(l2)

s='the quick brown fox jump over the lazy dog'
words=s.split()
print(words)

l=[[word.upper(),len(word)] for word in words]
print(l)

vowels=['a','e','i','o','u']
word=input('please enter here any string')
result=[]
for ch in word:
    if ch in vowels:
        if ch not in result:
            result.append(ch)
print(result)
print('no of unique vowels',len(result))

vowels=['a','e','i','o','u']
word=input('please enter here any string')
result=[]
for ch in vowels:
    if ch in word:
        result.append(ch)
print(result)
print('no of unique vowels',len(result))

l=[ch for ch in vowels if ch in word]
print(l)
