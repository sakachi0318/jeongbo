for i in range(int(input())):
    sumlist=[]
    numlist=[]
    numr=''
    sr=''
    num=input()
    for j in range(len(num)):
        numlist.append(num[j])
    numlist.reverse()
    for j in range(len(num)):
        numr+=numlist[j]
    s=str(int(num)+int(numr))
    for j in range(len(s)):
        sumlist.append(s[j])
    sumlist.reverse()
    for j in range(len(s)):
        sr+=sumlist[j]
    if s == sr:
        print(s+':True')
    else:
        print(s+':False')
