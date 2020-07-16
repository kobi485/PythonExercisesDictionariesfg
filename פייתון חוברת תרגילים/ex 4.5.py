list1=[]
a=int(input('enter number:'))
for i in range(a):
    if i<2:
        list1.append(i)
    else:
        list1.append(list1[i-1]+list1[i-2])
print(list1)