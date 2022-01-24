import random
com=random.randint(0,100)
print("시도횟수는 10번입니다.")
for i in range(1,11):
    k=int(input("%d."%(i)))
    if k==com:
        print("정답입니다~")
        break
    elif k<com:
        print("업")
    else:
        print("다운")
