for raw in range(8):
    for col in range(5):
        if (col==0 or col==4) or ((raw==0 or raw==3 or raw==7) and (col>0 and col<4)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()