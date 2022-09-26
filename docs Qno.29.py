list=[5,6,[],3,[],[],9]
i=0
while i<len(list):
    i=i+1
list.remove(list[2])
list.remove(list[3])
list.remove(list[3])
print(list)

