for i in range(int(input())):
    num=input()
    sum=int(num)+int(num[::-1])
    if str(sum) == str(sum)[::-1]:
        print('%d:True'%sum)
    else:
        print('%d:False'%sum)
