ans=[]
k=int(input())
for i in range(k):
    ans.append([])
    n,a=input().split(' ')
    n,a,b=int(n),int(a),0
    m=list(range(1,n+1))
    b+=a
    for j in range(len(m)):
        while b>len(m):
            b-=len(m)
        ans[i].append(m.pop(b-1))
        b+=a-1
for i in range(k):
    print(str(ans[i])[1:-1])
