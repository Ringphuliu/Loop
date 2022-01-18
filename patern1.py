n=int(input("enter the raw:"))
i=n
while i>=1:
    j=0
    while j<n-i:
        print("",end="")
        j+=1
    j=0
    while j<i:
        print("*",end="")
        j+=1
    i-=1
    print()