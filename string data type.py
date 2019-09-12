print('''hello
renuka 
how are you''')

print("hello how are 'you' and what are you doing")

print('hello how are \' are you')

print('''hello "hello" python how are 'you' and what are you doing''')

#how to access characters of the string:
#by using index or slicing
s='Shiva'
print(s[0])
print(s[-1])

s=input('please enter here any string!')
i=0
for x in s:
    print('The Character present at positive index:{} and at -ve index is:{} is {}'.format(i,i-len(s),x))
    i =i+1

#slice operator:
s='abcdefghijkl'
print(s[2:7])
print(s[2:0])
print(s[:])
print(s[:4])
print(s[2:])

#s[begine:end:step]

s='abcdefghij'
print(s[2:7:1])
print(s[2:7:2])
print(s[2:7:3])
print(s[::2])
print(s[::1])
print(s[::3])

print(s[3:7:-1])
print(s[::-1])
print(s[7:4:-1])
print(s[0:10000:1])
print(s[-4:1:-1]) #[begine to end+1]
print(s[-4:2:-2])
print(s[5:0:1])
print(s[-5:0:1]) #we will get 0 value because 0 is here
print(s[5:0:0])  #here we will get value error becaseu step values should not be 0
print(s[0:-10:-1])
print(s[0:-11:-1])
print(s[0:0:1]) # end valuse shoud not be 0 we will get empty values
print(s[0:-9:-2])
print(s[-5:-9:-2])
print(s[10:-1:-1])
print(s[1000:2:-1])

#mathematicals operators for string:
# + for concatenation
# * for repetation
print('renuka'+'hiren')
#print('renuka'+10) here we will get erro

print('shiva'*3)
print(3*'shiva')

#print('shiva'*3.0) we will get error becasue repetition is only aplicable only for int

#membership operator:
print('s' in 'shiva')
print('e' in 'shiva')
print('e' not in 'shiva')

s=input('enter mainstring here')
sub=input('enter here substring')
if sub in s:
    print('sub string is in mainstring')
else:
    print('sub string is not in mainstring')

#comparision operators for string:
#<,<=,>=,>,==,!=

print('renuka' < 'hiren')
print(ord('r'))
print(ord('h'))
print('renuka' >'hiren')

s1=input('enter first string')
s2=input(('enter second string'))
if s1==s2:
    print('both strings are same')
elif s1<s2:
    print('first string is less than second string')
else:
    print('fist string is greater than second string')

#removing spaces in string:

city=input('please enter your city name')
if city=='gujarat':
    print('hello gujarati')
elif city =='punjab':
    print('hello punjabi')
elif city=='mumbai':
    print('hello mumbai vasi')
else:
    print('please enter valid no here')

#lstrip(),rstrip(),strip()
city=input('please enter your city name')
scity=city.strip()
if scity=='gujarat':
    print('hello gujarati')
elif scity =='punjab':
    print('hello punjabi')
elif scity=='mumbai':
    print('hello mumbai vasi')
else:
    print('please enter valid no here')


city=input('please enter your city name').strip()
if city=='gujarat':
    print('hello gujarati')
elif city =='punjab':
    print('hello punjabi')
elif city=='mumbai':
    print('hello mumbai vasi')
else:
    print('please enter valid no here')

#finding substring:
#find(),rfind(),index(),rindex()
s='ABCBA'
print(s.find('B'))
print(s.find('X'))

print(s.rfind('B'))
print(s.rfind('X'))

s='ABCDEFGABCD'
print(s.find('B',3,8))
print(s.find('D',3,8))

#index() and rindex() to find string
s='ABCEDEF'
print(s.index('B'))
# print(s.index('Z')) we will get value error
print(s.rfind('E'))
# print(s.rfind('Z')) we will get value error

mail = input('enter your mail id')
try:
    i=mail.index('@')
    print('mail id contain @ symbol,which is mandartry')
except ValueError:
    print('mail id does not contain @ symbol and which is mandantory')

s='ABCDEFGABCD'
print(s.index('B',3,8))
print(s.index('D',3,8))
print(s.index('F',3,1000))

#counting substring in string:
s='ABBAABBBAECA'
print(s.count('A'))
print(s.count('BB'))
print(s.count('BBB'))
print(s.count('B',4,100))

s='BBBBBBBBBB'
print(s.count('B'))
print(s.count('BB'))
print(s.count('BBB'))
print(s.count('BBBB'))
print(s.count('BBBBBB'))

#To find index of all occurrence:
s='ABCABCABCA'
i=s.find('ABC')
print(i)
i=s.find('ABC',3,10)
print(i)
i=s.find('ABC',6,10)
print(i)
i=s.find('ABC',9,10)
print(i)

s='ABCABCABCA'
subs='ABC'
i=s.find(subs)
if i==-1:
    print('Secified Substring not found')
while i!=-1:
    print('{} present at index:{}'.format(subs,i))
    i=s.find(subs,i+len(subs),len(s))

s='ABCABCABCA'
subs=input('enter any string here')
i=s.find(subs)
if i==-1:
    print('Secified Substring not found')
while i!=-1:
    print('{} present at index:{}'.format(subs,i))
    i=s.find(subs,i+len(subs),len(s))
print('The number of occurences:',s.count(subs))

s='ABCABCABCA'
subs=input('enter here any sting')
i=s.find(subs)
if i==-1:
    print('Secified Substring not found')
c=0
while i!=-1:
    c=c+1
    print('{} present at index:{}'.format(subs,i))
    i=s.find(subs,i+len(subs),len(s))
    print('The number of occurences:', c)

#replacing string with one string to another
s='ABABABABAB'
s1=s.replace('A','B')
print(s1)

s='Shiva Patoliya'
s1=s.replace(' ','')
print(s1)
print('count no of space:',s.count(' '))
print('count no of spaces',len(s)-len(s1))

#replace method is case sensnitive
s='Learning Python is very Difficult'
s1=s.replace('Difficult','Easy')
print(s1)
print(s)

s='ABABABAABAB'
print('id of s before replacement',id(s))
s=s.replace('A','B')
print('id of s after replacement',id(s))

#splitting of string:
s='Shiva Patoliya Solution'
l=s.split()
print(l)
for x in l:
    print(x)

d='05-04-2019'
l=d.split('-')
print(l)
for x in l:
    print(x)
#joining of string:

l=['Hiren','Patoliya','Solution']
s=' '.join(l)
print(s)
s='-'.join(l)
print(s)
s=''.join(l)
print(s)

l=['05','04','2019']
s='-'.join(l)
print(s)
s=':'.join(l)
print(s)

#changing case of character of the string:
#upper(),lower(),swapcase(),title(),capitilize()

s='Learning Python is very Easy'
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.capitalize())

#check two strings are equal or not by ignoring case:
s1=input('enter first string')
s2=input('enter second string')
if s1.lower()==s2.lower():
    print('both strings are equal')
else:
    print('both are not equal')

s1=input('enter first string').lower()
s2=input('enter second string').lower()
if s1==s2:
    print('both strings are equal')
else:
    print('both are not equal')

#provided username and password are valid or not ?and username is not case sensitive but password is casesensitive
username=input('please enter here username').lower()
password=input('please enter here password')
if username=='Renuka' and password=='Shiva':
    print('valid username')
else:
    print('invalid username')

#first  and last character should be capital and remail will be lower
s=input('please enter here any string')
output=s[0].upper()+s[1:len(s)-1].lower()+s[-1].upper()
print(output)

#checking starting and endig of string:
s='Learning Python is very Easy'
print(s.startswith('Learning'))
print(s.startswith('Lear'))
print(s.startswith('L'))
print(s.endswith('Easy'))
print(s.endswith('y'))
print(s.endswith('asy'))

#to check type of character present in string or not:
print('Renuka38484'.isalnum())
print('Renuka88483'.isalpha())
print('shiva'.isalpha())
print('shiva'.isdigit())
print('28384'.isdigit())
print('shiv'.islower())
print('Shiva'.islower())
print('shiva123'.islower())
print('shiva'.isupper())
print('SHIVA'.isupper())
print('Shiva Patoliya Solution'.istitle())
print('Shiva patoliya Solution'.istitle())

#check the type of the character entered is from keyword:
s=input('enter here any string')
if s.isalnum():
    print('It is alphanumeric character')
    if s.isalpha():
        print('It is alphabet character')
        if s.islower():
            print('it is lower alphabec charactere')
        else:
            print('it is upper alphabec character')
    else:
        print('It is a digit')
elif s.isspace():
    print('It is space character')
else:
    print('It is not space character')