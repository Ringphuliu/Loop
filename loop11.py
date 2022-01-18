i=1
while i<=100:
    if i%3==0:
        print("nav")
    elif i%7==0:
       print ("gurukul")
    elif i%3==0 or i%7==0:
        print("navgurukul")
    else:
        print("number only")
    i=i+1
    print(i)
