#creation of dict
#empty dict
d={}
d=dict()
print(type(d))

#with data
d={'A':100,'B':200,'C':300}
print(d)
print(d['A'])

#by using dict
l=[(100,'A'),(400,'B'),(500,'C')]  #list of tuples
d=dict(l)
print(d)

t=((30,'A'),(400,'B'),(50,'C'))     #tuple of tuples
d=dict(t)
print(t)

s={(200,'B'),(500,'C'),(600,'D')}   #set of tuples
d=dict(s)
print(d)

l=[[100,'A'],[400,'B'],[60,'C']]    #list of lsit
d=dict(l)
print(d)

#here set of list is not possible because set is hashing code nd list is not hashing code
#dict in python
#map in c++ and java
#hash in perl and ruby

#by using dynamic input
d=dict(input('please enter here dict'))  #type here data in dict
print(d)

#access,add,update and delete data from th dictionary
#acess
d={100:'A',200:'B',300:'C'}
print(d[100])
print(d[300])
# print(d[700])   if key is not availabel then we will get keyvalu erorr
#if you do not want it we can write one program
d={100:'A',200:'B',300:'C',400:'D'}
key=int(input('enter here key value'))
if key in d:
    print('specific key value pair is ',d[key])
else:
    print('corresponidn values are not available')

#update
d={100:'Shiva',200:'Renuka',300:'Hiren'}
d[100]='Jaya'
print(d)
d[400]='Anu'
print(d)
d[500]='Shiva'
print(d)

#del
d={100:'Shiva',200:'Renuka',300:'Hiren',400:'jaya'}
del d[100]
print(d)
del d[300],d[200]
print(d)

#enter marks and name in dict and display result
n=int(input('enter no of student here'))
d={}
for i in range(n):
    name=input('enter here name of student')
    marks=input('enter here marks of student')
    d[name]=marks
print(d)
print('*'*30)
print('Name','\t\t','Marks')
print('*'*30)
for name in d:
    print(name,'\t\t',d[name])

#mathematical operators
#its not applicable in dict
d1={100:'Shiva',200:'Renuka',300:'Hiren'}
d2={200:'Renuka',400:'hiren',500:'diya'}
d3={200:'Renuka',300:'Hiren',100:'Shiva'}
#here d1+d2 and d1*3 is methametical operators and which is not applicable in dict

#equality operator
print(d1==d2)
print(d1==d3)

#Relational
#here relational operator is not applicable like
#d1>d2,d1>=d2,d1<d2,d1<=d2

#membership operator
print(100 in d1)
print(500 not in d2)

#len(),get(),update()
d={100:'Shiva',200:'Hiren',300:'Renuka'}
print(len(d))

print(d[100])
print(d[300])
# print(d[500]) here we will get keyvalue error but if we do not want it we have get method
print(d.get(100))
print(d.get(500))  #here we will get none default value and if we can set defualt values as per us
print(d.get(500,'guest'))
print(d)

#update()
d1={100:'shiva',200:'Hiren',300:'Renuka'}
d2={400:'Jaya',500:'Mira',600:'Anu',200:'diya'}
d1.update(d2)
print(d1)

#keys(),values() and item()
d={100:'Renuka',200:'Hiren',300:'Anu'}
print(d.keys())
for key in d.keys():
    print(key)

print(d.values())
for value in d.values():
    print(value)

print(d.items())
for item in d.items():
    print(item)

for k,v in d.items():
    print(k,"...." ,v)

#get value based on key and get key based on value
d={100:'A',200:'B',300:'C'}
key=int(input('enter key to get value:'))
if key in d:
    print('corresponding key value is:',d.get(key))
else:
    print('key value is not available')

#another ways
value=input('enter value to find key:')
available=False
for k,v in d.items():
    if v==value:
        print('coresponding key:',key)
        available=True
if available==False:
    print('The specified values not found in dict')

#pop(key)
d={100:'Shiva',200:'Renuka',300:'Anu'}
d.pop(100)
print(d)
d.pop(300)
print(d)
# d.pop(500) we will get erorr here
#d.pop(key,value)
d={100:'shiva',200:'Renuka',300:'Hiren'}
d.pop(100,'Gauest')
d.pop(500,'Guest')
print(d)

#d.popitem()
d={100:'shiva',200:'hiren',300:'renuka'}
print(d.popitem())
print(d.popitem())
print(d.popitem())
print(d)

d={100:'Renuka',200:'Shiva',300:'Hiren'}
d.clear()
print(d)

#setdefault()
d={100:'renuka',200:'Hiren',300:'Shiva'}
d[400]='Anu'
d.setdefault(500,'Hiren')
d.setdefault((100,'Renuka'))
print(d)

#aliasing and cloning:
#aliasing
d1={100:'Shiva',200:'Hiren',300:'Renuka'}
d2=d1
d1[400]='Anu'
print(d1)
print(d2)

#cloning
d1={10:'Hiren',20:'Anu',30:'Mira'}
d2=d1.copy()
d1[40]='Renuka'
d1[60]='Diya'
d2[50]='Nena'
print(d1)
print(d2)

#given input of dictionary write sum of that dict value
d={'A':100,'B':200,'C':300}
sum=0
for item in d.items():
    sum=sum+item[1]
print('total sum of given values are',sum)

d={'A':100,'B':200,'C':30,'D':400}
print('sum of given dict value',sum(d.values()))

#get the sum of give string in dict format
s='AAABBBCCDDEF'
d={}
for ch in s:
    d[ch]=d.get(ch,0)+1
print(d)
for k,v in d.items():
    print(k,v)

#get no of vowel in given string in dict form
word='HirenPatoliyaShivaPatoliyaRenukaPatoliya'
vowel={'a','e','i','o','u'}
d={}
for ch in word:
    if ch in vowel:
        d[ch]=d.get(ch,0)+1
for k,v in sorted(d.items()):
    print(k,'occured',v,'times')

#insert student marks and name and search for that application
n=int(input('enter here no of students:'))
d={}
for i in range(n):
    name=input('enter student name here')
    marks=int(input('entere marks of student'))
    d[name]=marks
print('student data insertion order is completed')
print('*'*30)
print('Name','Marks')
print('*'*30)
for k,v in d.items():
    print(k,'.....',v)
print('search operation started')
while True:
    name=input('enter student name to find marks here')
    marks=d.get(name,-1)
    if marks==-1:
        print('Student not found')
    else:
        print('Marks of ',name,'are:',marks)
    options=input('do you want to find another student marks[yes/no]:')
    if options=='no'.lower():
        break
    if options=='yes'.lower():
        continue
print('thank you for using our application ')

#comprehnsion
d={x:x*x for x in range(1,6)}
print(d)
d={x:2*x for x in range(1,6)}
print(d)

#merging of collections:
#list merging
l1=[10,20]
l2=[30,40]
print(l1+l2)
#l3=[*l1, *l2]
#print(l3)

#tuple merging
t1=(10,20)
t2=(30,40)
print(t1+t2)

#t3=(*t1,*t2)
#print(t3)

#set merging
s1={10,20,30}
s2={10,90,80}
# s1+s2 is not applicable
#s3=(*s1,*s2)
#print(s3)

#dict merging:
d1={100:'A',200:'B',300:'C'}
d2={300:'D',600:'E'}
# d1+d2 is not applicable

#d3={**d1,**d2}
#print(d3)

#nested collections introduction and examples:
#list nested colelction
l=[(10,30,40),(30,40,50)]
print(l[1][0])
print(l[0][2])

#dict nested collection
d={'cars':('Innova','Honda','maruti'),'mobiles':('samsund','nokia','iphone')}
print(d.get('cars')[1])
print(d['cars'][0])
for mobile in d.get('mobiles'):
    print(mobile)

#good application:
supermarket={
    'Store1':{
        'Name':'Renuka general store',
        'Items':[
    {'Name':'soap','quantity':20},
    {'Name':'brush','quantity':30},
    {'Name':'pen','quantity':40}
]
},
'store2':{
    'Name':'Grocery Store',
    'Items':[
    {'Name':'Mint','Quantity':10},
    {'Name':'Spinach','Qaunity':20},
    {'Name':'potatoes','Qauntity':40}
]
}
}
print('name of the store1 name')
print(supermarket.get('Store1').get('Name'))
print(supermarket['Store1']['Name'])

print('all presents supermarkets items name')
for d in supermarket['Store1']['Items']:
    print(d['Name'])
print('print no of spinach in quantity in store2')
for d in supermarket['store2']['Items']:
    if d['Name']=='Spinach':
        print(d['quantity'])

#list inside set and dict:
#in dict key should not be list because key in dict followed hashcode
#but value could be list because it does not follow hashcode







