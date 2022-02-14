import numpy
critics={
    'BTS':{'암수살인':5, '바울':4, '할로윈':1.5},
    '손흥민':{'바울':5, '할로윈':2},
    '레드벨벳':{'암수살인':2.5, '바울':2, '할로윈':1},
    '트와이스':{'암수살인':3.5, '바울':4, '할로윈':5},
}
final=10
for i in critics:
    if i=='BTS':
        continue
    else:
        t=critics[i]
        m=0
        for j in t:
            x=critics['BTS'][j]-critics[i][j]
            x2=x*x
            m+=x2
        ans=math.sqrt(m)
        if ans<final:
            final=ans
            fans=i
print(fans)
