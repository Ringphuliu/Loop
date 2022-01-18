for raw in range(5):
    for col in range(5):
        if (raw==0 or raw==4)or (col==0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()