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