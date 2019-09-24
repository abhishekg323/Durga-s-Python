#set data structure
#duplicates are not allowed
#order is not applicable
#indexing and slicing is not applicable
#represented by {}
#heterogenous
#mutable
#empty {} is by default dict not set becasue dict is most common used
s={}
print(type(s))
s=set()
s.add(10)
s.add('Z')
print(s)
s.add(20)
s.add('A')
s.add(10) #duplicates are not allowed and it will not added
print(s)

#creation of set object:
#empy set
s={}     # it will be dict
s=set()
print(type(s))

#with data
s={10,20,30,40,50}
print(s)
s={'Shiva Patoliya'}
print(s)

#by using set() function
l=[10,20,30,40,50]
s=set(l)
print(s)
print(l)

s=set(range(0,101,10))
print(s)

s=set(input('please etenre here any value'))
print(s)

s='Apple'
s1=set(s)
print(s1)

#mathematical,equality,relational,membership operator for set
#mathematical operator
# s1 + s2 is not applicable
#s1 * 3 also not applicable or we can not apply

#equality operator(==,!=)
s1={10,20,30}
s2={40,50,60}
print(s1==s1)
print(s1!=s2)

#relational operator
s1={10,20,30,40,50,60}
s2={20,30,40,50,30}
print(s1<s2)
print(s1>s2)
print(s1<=s2)
print(s1>=s2)

#membership
s1={10,20,40,50}
print(10 in s1)
print(20 not in s1)
print(10 not in s1)
print(90 not in s1)

#len() is python inbuilt function
s={10,20,30,'shiva'}
print(len(s))

#add()
s={10,20,40}
s.add('Hiren')
s.add('Shiva')
s.add(50)
print(s)

#update()
s={10,20,30,40}
s1={50,60}
s2={70,80}
s.update(s1,s2)
print(s)

s={50,60}
l=[10,30]
s.update(l)
print(s)
s.update(range(1,6,2))
s.update(range(1,20,10),range(3,50,12))
s.update(range(1,20,5),'Shiva')
print(s)
#in add() we can add only one elements but in update() we can add more than one iterable object

#remove(),discard(),pop() and clear()
s={10,20,30,40,50}
s.remove(10)
s.remove(40)
print(s)
# s.remove(60) here 60 is not available in set list so it will give error
#if we do not want like that erorr then we can happily used discard()

s={10,20,30,40,50,60}
s.discard(20)
s.discard(30)
s.discard(70) #here 70 is not in set but we will not get error in discard()
print(s)

#pop() it will remove first or last element from set but there is not garuntee that first one will remove or last one
s={10,30,40,60,70,80}
s.pop()
print(s)
s.pop()
s.pop()
print(s)

#union(),intersection(),difference() and symmetric_difference()
#union
s1={10,20,30,50,60}
s2={30,50,30,50,60,20,60,70,80}
s=s1.union(s2)
print(s)

s=s1|s2
print(s)

#intersection()
s1={10,20,30,40,50,60}
s2={40,50,60,70}
s3=s1.intersection(s2)
print(s3)
s3=s1&s2
print(s3)

#difference()
s1={10,20,30,40}
s2={30,40,50,60}
print(s1.difference(s2))
print(s1-s2)

#symmetric_difference()
s1={10,20,30,40}
s2={30,40,50,60,70}
print(s1.symmetric_difference(s2))
print(s1^s2)

#aliasing ,cloning,comprehnsion
s1={10,20,30,40,50}
s2=s1 #aliasing
print(s2)
print(s1)

s3=s1.copy() #cloning
print(s3)

#comprehnsion
s={x*x for x in range(1,6)}
print(s)

s={2*x for x in range(1,10)}
print(s)

s={3*x for x in range(1,10)}
print(s)

#write program to delet duplictes from list
#by converting list into set
l=[10,30,40,50,40,10,30,30]
s=set(l)
print(s)
l1=list(s)
print(l1)

#another way
l=[10,20,30,10,20,30]
l1=[]
for x in l:
    if x not in l1:
        l1.append(x)
print(l1)

#write vowel into list from given input
l=input('please enter here')
s=set(l)
v={'a','i','e','o','u'}
result=s.intersection(v)
print(result)

