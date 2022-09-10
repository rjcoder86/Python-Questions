n=5
l=[]
for i in range(1,n+1):
    c=1
    l1=[]
    for j in range(1,i+1):
        # print(c,end='')
        l1.append(c)
        c=c*(i-j)//j
    l.append(l1)
    # print()
print(l)
