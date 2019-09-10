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


