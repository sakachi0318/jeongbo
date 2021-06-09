#1412성준호
n=int(input())
k=input()
dummy=[]
anslist=[]
for i in range(n):
    c=[]
    ans=[]
    b=97
    a=list(input())
    while len(a)%len(k)!=0:
        a.append(chr(b))
        b+=1
    d=0
    while len(a)!=0:
        c.append(list(a[:len(k)]))
        for j in range(len(k)):
            if len(a)!=0:
                dummy.append(a.pop(0))
                dummy.clear()
            else:
                break
    for j in range(len(c)):
        for l in range(len(k)):
            ans.append(c[j][int(k[l])-1])
    ansint='#%d '%(i+1)
    for j in range(len(ans)):
        ansint+=ans[j]
    anslist.append(ansint)
for i in range(len(anslist)):
    print(anslist[i])
