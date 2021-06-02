import math
import time
while True:
    print('소수 판독 by sorami takaoka')
    ins=(int(input('숫자를 입력하세요(0=종료:)')))
    a=2
    if ins==0:
        print('이용해 주셔서 감사합니다.')
        time.sleep(1)
        quit()
    while True:
        if math.sqrt(ins)<a:
            print('%d는 소수입니다.'%ins)
            break
        elif ins%a==0:
            print('%d는 소수가 아닙니다.'%ins)
            break
        else:
            a+=1
            continue
    print('===========================================')
    
