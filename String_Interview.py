#write program to reverse given string by using slice operator
s='Shiva'
output=s[::-1]
print(output)

s=input('please enter here any string:')
output=s[::-1]
print(output)

#write program to reverse given string by using reversed()
s='Shiva'
r=reversed(s)
print(type(r))
output=''.join(r)
print(output)

s=input('please enter here any string')
r=reversed(s)
for ch in r:
    print(ch)

#write program to reverse given string by using while loop
s='Renuka'
output=''
i=len(s)-1
while i>=0:
    output=output+s[i]
    i=i-1
print(output)

#write program to reverse order of words
s='learning python is very easy'
l=s.split()
print(l)
l1=l[::-1]
print(l1)
output=' '.join(l1)
print(output)

#write program to convert internal word of the string
s="learning python is very easy"
l=s.split()
print(l)
l1=[]
for word in l:
    l1.append(word[::-1])
print(l1)
ouput=''.join(l1)
print(output)


#write program to reverse every second words in the string list:
s='one two three four five six seven eight nine ten'
l=s.split()
i=0
l1=[]
while i<len(l):
    if i%2==0:
        l1.append(l[i])
    else:
        l1.append(l[i][::-1])
    i=i+1
    output=' '.join(l1)
print(output)

#
s=input('please enter here any string')
i=0
print('character present at even index')
while i<len(s):
    print(i)
    i=i+2
print('character present at odd index')
i=1
while i<len(s):
    print(i)
    i=i+2

#different ways
s=input('enter here any no')
print('print here even no:',s[0::2])
print('print here odd no:',s[1::2])
