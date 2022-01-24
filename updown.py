import random
com=random.randint(0,100)
i=1
while True:
    k=int(input("%d."%(i)))
    if k==com:
        print("정답입니다~")
        break
    elif k<com:
        print("업")
    else:
        print("다운")
    i+=1       
print("시도횟수는 %d번입니다."%(i))
