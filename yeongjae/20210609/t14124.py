#1412 성준호
gicho=[1,7,5,5,2,0,3,3,7,2,0,1,9,8,0,2,2,1,5,7,3]
a=[]
b=0
for i in range(len(gicho)):
    if gicho[i]==0:
        a.append(list(gicho[b:i]))
        b=i+1
a.append(list(gicho[b:]))
for i in range(len(a)):
    a[i].sort()
    print('%d:'%len(a[i])+str(a[i]),sep='')
