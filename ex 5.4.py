
num=0
numm=0
line=input('enter number:').split()
for i in line:
    if 59<int(i)<101:
        num+=1
    elif 0<=int(i)<60:
        numm+=1
print(num)
print(numm)



