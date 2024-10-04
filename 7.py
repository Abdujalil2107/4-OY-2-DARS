n = int(input("N: "))
i = 0
while n!=0:
    i = i*10+n%10
    n//=10
while i!=0:
    print(f"{i%10}",end=" ")
    i//=10
