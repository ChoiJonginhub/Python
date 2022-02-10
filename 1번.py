#1.
name='이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌'
names=name.split(",")
# 1)
kim=0
lee=0
for i in names:
    t=list(i)
    if(t[0]=='김'):
        kim+=1
    elif(t[0]=='이'):
        lee+=1
print("김씨: %d명, 이씨: %d명"%(kim, lee))
# 2)
lee=0
for i in names:
    if(i=='이재영'):
        lee+=1
print("이재영은 %d명"%(lee))
# 3)
print(set(names))
# 4)
x=list(set(names))
print(sorted(x))