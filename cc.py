n=int(input("enter the number:"))
k=ord("A")
for i in range(n):
    for j in range(i+1 ):
        print(chr(k),end=" ")
        k=k+1
    print()


# n=int(input("enter the number:"))
# for i in range(n):
#     k=ord("A")+i
#     for j in range(i+1):
#         print(chr(k),end=" ")
#         k=k+1
#     print()

# n=int(input("enter the number:"))
# for i in range(n):
#     k=ord("A")
#     for j in range(i+1):
#         print(chr(k),end=" ")
#         k=k+1
#     print()