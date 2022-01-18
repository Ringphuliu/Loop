for raw in range(5):
    for col in range(5):
        if (raw==0 or raw==4)or(raw==1 and col==3)or (raw==2 and col==2)or(raw==3 and col==1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()