n = 7

for i in range(0,n):
    for j in range(0, i):
        print(" ", end = " ")
    for j in range(0, (n-i)*2-1):
        print("*", end = " ")
    for j in range(0, i):
        print(" ", end = " ")
    print()