for i in range(int(input())):
    num=input()
    s=int(num)+int(num[::-1])
    if str(s)==str(s)[::-1]:print('%d:True'%s)
    else:print('%d:False'%s)
