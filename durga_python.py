import keyword
print(keyword.kwlist)

#list
'''Lists can contain millions of items, so Python provides an
efficient way to loop through all the items in a list. When
you set up a loop, Python pulls each item from the list one
at a time and stores it in a temporary variable, which you
provide a name for. This name should be the singular
version of the list name.
 The indented block of code makes up the body of the
loop, where you can work with each individual item. Any
lines that are not indented run after the loop is completed. '''
''' 
#List data type(collection related data type) and is mutable
#order preserved and duplicates are allowed and values should be in [], indexes and sliceing
# concept is available, growable in nature and mutable
'''
#looping through list

#printing all item in list
users = ['anu','mira','dia','nena','renuka','hiren']
for user in users:
    print(user)

#Printing a message for each item, and a separate message afterwards
for user in users:
     print('Welcome,' + user + '! ' )

print('Welcome, we are glad to see you all!')

#the range function
'''You can use the range() function to work with a set of
numbers efficiently. The range() function starts at 0 by
default, and stops one number below the number passed to
it. You can use the list() function to efficiently generate a
large list of numbers'''
#printing the number 0 to 10
for number in range(10):
    print(number)   #its printing too many

#pringing number from 1 to 10
for number1 in range(1,11):
    print(number1)

#Making a list of numbers from 1 to 101
numbers = list(range(1,101))
print(numbers)
users = ['hiren','shiva','renuka']
for user in users:
    print('welcome to ' + user + '!')
print('I really happy to see all users here!')

bikes = ['trek','redline','giant']
for bike in bikes:
    print(bike)

#adding item to list
squares = []
for x in range(1,12):
    squares.append(x**2)

print(squares)

squares1 = []
for x in range(1,12):
    print(x)

#list comprehnsion
'''You can use a loop to generate a list based on a range of
numbers or on another list. This is a common operation, so
Python offers a more efficient way to do it. List
comprehensions may look complicated at first; if so, use the
for loop approach until you're ready to start using
comprehensions.
 To write a comprehension, define an expression for the
values you want to store in the list. Then write a for loop to
generate input values needed to make the list.'''

squares2 = [x**2 for x in range(1,12)]
print(squares2)

names = ['kai', 'abe', 'ada', 'gus', 'zoe']

upper_names = []
for name in names:
    (upper_names.append(name.upper()))

print(upper_names)

#Using a comprehension to convert a list of names to upper case
names = ['kai', 'abe', 'ada', 'gus', 'zoe']
upper_names = [name.upper() for name in names]

print(upper_names)

#visulizing your code
'''When you're first learning about data structures such as
lists, it helps to visualize how Python is working with the
information in your program. pythontutor.com is a great tool
for seeing how Python keeps track of the information in a
list. Try running the following code on pythontutor.com, and
then run your own code.'''
dogs = []
dogs.append('whillie')
dogs.append('hootz')
dogs.append('peso')
dogs.append('goblin')

for dog in dogs:
    print('hello' + dog + '!')
print('I love these dogs!')

print("\nThese were my first two dogs:")
old_dogs = dogs[:2]

for old_dog in old_dogs:
    print(old_dog)

#deleting,removing,adding,slicing,indexing operation on list
del dogs[0]
dogs.remove('peso')
print(dogs)

l=[]
l.append(10)
l.append(20)
l.append(30)
l.append(40)
print(l)

l.remove(30)
print(l)

l.append(20)
print(l)

l[0] = 777
print(l)

bikes = ['trek','redline','giant']
print(bikes[0])
print(bikes[-1])

#mutable concept
list1 = [10,20,30,40]
print(list1)
print(id(list1))
list1[0] = 70
print(list1)
print(id(list1))

l1=[10,20,30,40]
l2 =l1
print(l1)
print(l2)

l1[0] = 7777
print(l1)
print(l2)

l2[1]= 888
print(l1)
print(l2)

#slicing list
l=[10,'Shiva',20,30,10]
print(type(l))
print(l)
print(l[0])
print(l[-1])
print(l[1:4])

#making list
users = ['val','bob','mia','ron','ned']
print(users)

#changing element
users[0]='valeri'
users[-2] = 'ronald'
print(users)

#adding elements to end of the list
users.append('amy')

#inserting element at particular position
users.insert(0,'Joe')
users.insert(3,'bea')
print(users)

#removing elements
del users[-1]
users.remove('mia')

#pop
'''If you want to work with an element that you're removing
from the list, you can "pop" the element. If you think of the
list as a stack of items, pop() takes an item off the top of the
stack. By default pop() returns the last element in the list,
but you can also pop elements from any position in the list.'''
print(users.pop())
print(users.pop(0))
print(users)

#list length
print(len(users))
leng = len(users)
print(leng)
print('we have '+str(leng)+' '+'users')

#sorting list
users.sort()
print(users)

#Sorting a list permanently in reverse alphabetical order
users.sort(reverse=True)
print(users)
users.sort(reverse=False)
print(users)

#reversing the order of list
users.reverse()
print(users)

#looping through list

#finding minimum value in list
ages = [12,34,45,34,22,36,12,30,28,26,20]
print(min(ages))
print(max(ages))
print(sum(ages))

#changing elements
l = ['hiren','nena','diza']
l[0] = 'Renuka'
print(l)

finishers=['renu','shiva','hiren','diya']
print(finishers[:2])

#copying list
copy_of_finishers = finishers[:]
print(copy_of_finishers)

#adding items to list
