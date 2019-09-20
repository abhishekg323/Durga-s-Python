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