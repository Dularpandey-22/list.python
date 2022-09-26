a=[(8102849704)]
b=str(a)
i=1
while i<len(b):
    c=b[i]+b[i+1]+b[i+2]
    d=b[i+3]+b[i+4]+b[i+5]
    e=b[i+6]+b[i+7]+b[i+8]+b[i+9]
    if int(c)>=100 and int(c)<=999:
        if int(d)>=100 and int(d)<=999:
                print("("+c+")"+d+"-"+e)
                break
    i=i+1




n=int(input("enter the number of rows:"))
i=10
while i<=n*10:
          j=i
          while j>=10:
                    print(j,end=" ")
                    j=j-10
          i=i+10
          print()