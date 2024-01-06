n=6
for i in range(2,n+1):
    if (i%2 != 0):
         a=1
    else:
        a=0
    for j in range(1,i):
        print(a, end = " ")
        a = 1 - a
    print()

def whatidid():
 print(1)
 for i in range(2,n+1):
    for j in range(1,i):
        if (i%2 != 0):
         a=1
         print(a,end = " ")
         print(a-1,end = " ")
        else:
           a=0
           print(a,end = " ")
           print(a+1,end = " ")
    print()