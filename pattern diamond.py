# n =3

n = int(input("Please enter number : ".strip()))

def tri():
    for i in range(0,n):
        for j in range(0,n-i-1):
            print(" ", end = " ")
        for j in range(0,2*i+1):
            print("*", end = " ")
        for j in range(0,n-i-1):
            print(" ", end = " ")
        print()

def inv_tri():
    for i in range(0,n):
         for j in range(0,i):
             print(" ", end = " ")
         for j in range(0,(n-i)*2-1):
             print("*", end = " ")
         for j in range(0,i):
             print(" ", end = " ")
         print()

tri()
inv_tri()