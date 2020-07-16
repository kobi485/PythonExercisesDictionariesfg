
from random import randint
l=0
h=100
r=randint(l,h)
print(r)
answe=input('is the guess correct')
while answe!='correct':
    if answe=='low':
        l=r
    else:
        h=r
    r=randint(l,h)
    print(r)
    answe=input('is the guess correct')
print('finish')