#2.
ver="1.2.0,1.1.99"
v=ver.split(",")
a=[]
for i in v:
    k=i.split(".")
    b=[]
    for j in k:
        b.append(int(j))
    a.append(b)
for i in range(0, len(a[0])):
    if(a[0][i]>a[1][i]):
        print(v[0],">", v[1])
        break
    elif(a[0][i]<a[1][i]):
        print(v[0], "<", v[1])
        break