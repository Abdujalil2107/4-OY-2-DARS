a,b,c=0,0,0
for i in range(100,1000):
    a=i%10
    b=i//10%10
    c=i//100%10
    if a==b or a==c or b==c:
        print(i,end=" ")
    a,b,c=0,0,0