n=6

for i in range(1,n+1):
    a=1
    b=0
    for j in range(0,i):
        print(a,end = " ")
        a +=1
    for j in range(0,(n-i)*2):
        print(" ", end = " ")
    for j in range(0,i):
        print(i-b ,end = " ")
        b +=1
    print()
