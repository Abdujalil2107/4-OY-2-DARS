tub=1
for i in range(2,100):
    for j in range(2,i+1):
        if i%j==0:
            tub+=1
    if tub==2:
        print(i)
    tub=1