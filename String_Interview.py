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

#write program to merge two similar string:
s1='Shiva'
s2='Patol'
i,j=0,0
output=''
while i<len(s1) or j<len(s2):
    output=output+s1[i]+s2[j]
    i=i+1
    j=j+1
print(output)

s1='Shiva'
s2='Patoliya'
i,j=0,0
output=''
while i<len(s1) or j<len(s2):
    if i<len(s1):
        output=output+s1[i]
        i=i+1
    if j<len(s2):
        output=output+s2[j]
        j=j+1
print(output)

#sorted one string with alphabetic and digital in one string
s='12AB34CD'
print(sorted(s))
alphabetic=[]
digital=[]
for ch in s:
    if ch.isalpha():
        alphabetic.append(ch)
    if ch.isdigit():
        digital.append(ch)
output=''.join(sorted(alphabetic)+sorted(digital))
print(output)

#converted digital symbol in alphabet
s='A4B3C2D'
output=''
for ch in s:
    if ch.isalpha():
        x=ch
    else:
        d=int(ch)
        output=output+x*d
print(output)
#use here sorted string
target=''.join(sorted(output))

#convert aaaabbbccz in 4a3b2c1z
s='aaaabbbccz'
previous=s[0]
c=1
i=1
output=''
while i<len(s):
    if s[i]==previous:
        c=c+1
    else:
        output=output+str(c)+previous
        previous=s[i]
        c=1
    if i==len(s)-1:
        output=output+str(c)+previous
    i=i+1
print(output)

#convert a4k3c2 in aebnce
s='a4k3c2'
output=''
for ch in s:
    if ch.isalpha():
        output=output+ch
        x=ch
    else:
        d=int(ch)
        newchr=chr(ord(x)+d)
        output=output+newchr
print(output)

#remove duplicates from string
s="ABBCCDDAEGHDHHDFFIIJKLMOOPQQSSTUWYZFNHHRXDFVBFG"
output=''
for ch in s:
    if ch not in output:
        output=output+ch
output1=' '.join(sorted(output))
print(output1)

#other way
s='ABBCCDDEEFF'
l=[]
for ch in s:
    if ch not in l:
        l.append(ch)
l1=''.join(sorted(l))
print(l1)

#another way
s='ABBCCDDEEFFF'
s1=set(s)
print(s1)
s2=''.join(sorted(s1))
print(s2)

#how many times string are occured in string
s='AABBLLLCCCDDDD'
l=[]
for ch in s:
    if ch not in l:
        l.append(ch)
for ch in sorted(l):
    print('{} occure {} time '.format(ch,s.count(ch)))

#other ways
s='AABDEFFFEE'
s1=set(s)
for ch in s1:
    print('{} occure {}'.format(ch,s.count(ch)))

s='AABBCCDD'
for ch in (s):
    print('{} occures {}'.format(ch,s.count(ch)))


