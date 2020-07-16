from random import randint
list2=randint(1,9)
a=int(input('enter number:'))
while a!=list2:
    if a>list2:
        print('try lower')
    elif a<list2:
         print('try high')
    a = int(input('enter number:'))
else:
    print('graet')








