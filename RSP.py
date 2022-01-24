import random
com=random.randint(0,2)
if com==0:
    com2="가위"
elif com==1:
    com2="바위"
else:
    com2="보"
user=int(input("하나를 선택하세요 : 가위(0), 바위(1), 보(2) :"))

print("컴퓨터는 %s를 냈습니다."%(com2))
if user==com:
    print("비겼습니다.")
elif user<com:
    if user==0 and com==2:
        print("당신이 이겼습니다.")
    else:
        print("당신이 졌습니다.")
elif user==2 and com==0:
    print("당신이 졌습니다.")        
else:
    print("당신이 이겼습니다.")
