l=[[10, 20], [30, 40], [50, 60], [30, 20, 80]]
l1=[[61], [12, 14, 15], [12, 13, 19, 20], [12]]
i=0
a=[]
while i<len(l):
    b=l[i]+l1[i]
    a.append(b)
    i=i+1
print(a)