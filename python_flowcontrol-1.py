#break statement:
#if break statement can not possible without for or while loop
for i in range(10):
    if i==7:
        print('processing is enough, break loop execution')
        break
    print(i)
print('out side of loop')

cart =[10,20,30,600,40,50]
for item in cart:
    if item>500:
        print('iteam is more than 500,so its reqired insurance,we can not go further')
        break
    print('processing item',item)

# x=10
# if x>40:
#     print('we are stopping program execution')
#     break
# print('hello')

#continue statement:
for i in range(10):
    if i%2==0:
        print(i)
        break
    print('hello')

#in continue:
for i in range(10):
    if i%2==0:
        continue
    print(i)

for i in range(10):
    if i%2!=0:
        continue
    print(i)

cart = [10,20,30,40,503,60,600]
for item in cart:
    if item>500:
        print('please skipped this item because its required insurance')
        continue
    print('processing item',item)

l=[10,20,0,40,30,50]
for x in l:
    print('100/{}={}'.format(x,100/x))

l=[10,20,0,40,30,50]
for x in l:
    if x==0:
        print('how it it possible divided by zero')
        continue
    print('100/{}={}'.format(x,100/x))

#here, we will get error because without for or while loop we can not use continue or break statements
# x=10
# if x>40:
#     print('hello')
#     continue
# print('hi')

#break and continue in loop
for i in range(3):
    for j in range(3):
        if i==j:
            break
        print(i,j)

for i in range(3):
    for j in range(3):
        if i==j:
            continue
        print(i,j)

#loops with else block:
cart = [10,20,30,40,50]
for item in cart:
    if item>500:
        print('we can not process this item because it required insurance')
        break
    print('processing iteam in progress',item)
else:
    print('congratualtions your all item succeessfully process')

#break
cart = [10,20,30,40,50,600]
for item in cart:
    if item>500:
        print('we can not process this item because it required insurance')
        break
    print('processing iteam in progress',item)
else:
    print('congratualtions your all item succeessfully process')

#break
cart = [10,20,30,40,50,600,50,60]
for item in cart:
    if item>500:
        print('we can not process this item because it required insurance')
        break
    print('processing iteam in progress',item)
else:
    print('congratualtions your all item succeessfully process')

#continue
cart = [10,20,30,40,50,600,50,60]
for item in cart:
    if item>500:
        print('we can not process this item because it required insurance')
        continue
    print('processing iteam in progress',item)
else:
    print('congratualtions your all item succeessfully process')

#pass statement:
