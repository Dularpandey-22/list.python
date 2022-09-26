# a="my3 na7me i8s A9ariya"
# i=0
# b=""
# while i<len(a):
#     if a[i].isdigit():
#         pass
#     else:
#         b=b+a[i]
#     i=i+1
# print(b)

a=[20,8,12,7,78,92,15]
i=0
b=[]
while i<len(a):
    n=0
    while n<1000:
        j=0
        while j<len(a):
            if a[j]==n:
                b.append(a[j])
            j=j+1
        n=n+1
    i=i+1
    break
print(b)