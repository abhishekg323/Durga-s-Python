#Tuple
#order is applicable
#duplicates are allowed
#Heterogeneous object
#Indexing and slicing
#Immutable
#()
t=('Shiva',10,20,30,'Hiren')
print(type(t))
print(t[0])
print(t[3])

t=(10,20,30)
print(type(t))
t=(10,20)
print(type(t))
t=(10)
print(type(t))

#single value tuple
t=(10,)
print(type(t))
t=()
print(type(t))
t=(10)
print(type(t))
t=10
print(type(t))
t=(10,)
print(type(t))
t=10,
print(type(t))
t=(10,20,30)
print(type(t))
t=10,20,30,40
print(type(t))
t=(10,20,30,)
print(type(t))
t=10,20,30,
print(type(t))

#creation of tuple object
#empy tuple
t=()
#single value tuple
t=(10,)
print(t)
#multiple value tuple
t=(10,20,30)
print(t)
t=10,20,30,
print(t)
t=10,20,30
print(t)
t=(10,20,30,)
print(t)
#tuple function
t=tuple(input('enter here any no'))
print(t)

l=[10,20,30]
t=tuple(l)
print(type(t))
print(t)

t=tuple(range(1,11,2))
print(t)

t='Shiva Patoliya'
t1=tuple(t)
print(t1)

t=tuple('Hiren Patoliya')
print(t)


#with dynamic input
t=tuple(input('please enter here anything'))
print(t)

#accessing elements of tuple by using index and slicing operator
#by using index
t=(10,30,40,50,50)
print(t[0])
print(t[-1])
print(t[1])

#by using slice
t=(10,20,30,40,50,50,60,70)
print(t[::])
print(t[::2])
print(t[1:3])
print(t[::-1])
print(t[2:5])

#mathematicals operators for tuple
#concatenation and repetation operator
t1=(10,20)
t2=(30,40)
print(t1+t2)
#here we can concatenate only with tuple not any thing else
print(t1+(10,20))

print(t1*2)
t3=t1*3
t4=t3+t2
print(t4)
print(t3)

#equality, relational and membership operator in tuple
#equality operator: ==,!=
t1=('Shiva','Hiren','Renuka','Jaya')
t2=('Shiva','Hiren','Renuka','Jaya')
t3=('SHIVA','HIREN','RENUKA','JAYA')
t4=('Shiva','Jaya','Renuka','Hiren')
print(t1==t2)
print(t1==t3)
print(t1==t4)
print(t1!=t2)
print(t1!=t3)

#relational operator:<,<=,>,>=
t1=(10,20,30,40)
t2=(40,20,10,30)
t3=(10,30,20,30)
print(t1<t2)
print(t1>t2)
print(t<=t2)
print(t1>=t2)

#membership operator: in and not in
print(10 in t1)
print(10 not in t1)
print(50 in t1)
print(50 not in t1)

#methods and functions in tuple:count(),len() and index()
#len()
t=(10,20,30,40,50)
print(len(t))

#count()
t=(10,20,20,30,30,30,30,40,50)
print(t.count(10))
print(t.count(30))
print(t.count(40))

#index()
t=(10,20,30,40,50)
print(t.index(20))
print(t.index(50))

#reversing and sorting elements of tuple
# here reverse method is not applicable
#reversed
t=(1,2,3,4,5,6,7,8,9)
l=reversed(t)
t1=tuple(l)
print(t1)

#sorted
t=(1,2,3,4,5,6,7,8,9)
l=sorted(t)
print(tuple(l))

#sorted with reverse
t=(1,2,3,4,5,6,7,8,9)
l=sorted(l,reverse=True)
print(tuple(l))

#max() and min()
t=(10,20,40,50,60,07,400)
print(max(t))
print(min(t))

#tuple packing and unpacking method
a=10
b=20
c=30
d=40
t=a,b,c,d
print(t)
l=[a,b,c,d]
print(l)

t=(10,20,30,40)
a,b,c,d=t
print(a,b,c,d)
print(a)
print(b)

#comprehnsion tuple
t=(x*x for x in range(1,6))
print(type(t))
print(t)

#in list
l=[x*x for x in range(1,6)]
print(l)

#difference between list nd tuple
#list is unhashable and tuple is hashable
# in set and dict we can add tuple but can not add list
import collections
t=(10,20,30,40)
l=[10,20,30,40]
print(isinstance(t,collections.Hashable))
print(isinstance(l,collections.Hashable))
print(hash(t))
# print(hash(l)) we will get error like is unhashable

s={10,20}
t=(30,40)
l=[50,60]
s.add(70)
print(s)
s.add(t)
print(s)
# s.add(l) we can not add list to set

d={}
t=(10,30,40,50)
l=[30,40,50,60]
d[t]='A'
print(d)
d[l]='B'
print(d)


#write program to get sum and average value of give input
t=tuple(input('enter here any no'))
sum=0
for x in t:
    sum=sum+x
print('the sum:',sum)
print('average',sum/len(t))

t=eval(input('enter here number in tuple'))
print('sum of given tuple',sum(t))
print('average of given tuple',sum(t)/len(t))

