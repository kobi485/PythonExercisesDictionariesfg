line1=[]
sum=0
for i in range(5):
    num=int(input('enter nuumber:'))
    line1.append(num)
    sum+=num
print(max(line1))
print(min(line1))
print(sum/(len(line1)))


