for raw in range(8):
    for col in range(5):
        if (col==0 or col==4)or(raw==3):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()