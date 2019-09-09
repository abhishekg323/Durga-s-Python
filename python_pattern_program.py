#pattern application
n= int(input('enter n value'))
for i in range(n):
    print('*')

# n= int(input('enter n value'))
# for i in range(n):
#     print('*',end=' ')

#to print squere pattern with * symbol
n= int(input('enter no of rows'))
for i in range(n):
    print('* ' *n)

#to print square pattern with provided fixed digit in every row:
n = int(input('please enter here any number:'))
for i in range(n):
    print((str(i+1)+' ')*n)

#to print square pattern with alphabet symbol
n = int(input('please enter here any number'))
for i in range(n):
    print((chr(65+i)+' ') * n)

#right angle tiragle
n=int(input('please enter no here:'))
for i in range(n):
    for j in range(i+1):
        print('*',end='' )
    print()

#print reverse of right trianle
n= int(input('please enter the no'))
for i in range(n):
    print('* '*(n-i))

#to print pyramid pattern with *
n = int(input('please enter here any no here'))
for i in range(n):
    print(' '*(n-i-1) + '* '*(i+1))

#inverted pyramid
n= int(input('please enter here any no here'))
for i in range(n):
    print(' ' * i + '* '*(n-i))

#to print diamond pattern with *:
n=int(input('please enter here no:'))
for i in range(n):
    print(' '*(n-i-1)+'* '*(i+1))
for i in range(n-1):
    print(' '*(i+1)+'* '*(n-i-1))