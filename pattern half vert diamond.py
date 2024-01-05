num = int(input("Please enter the num : ").strip())


def tri():
    for i in range(0,num+1):
        for j in range(0,i):
            print("*", end =" ")
        print()

def inv_tri():
     for i in range(0,num+1):
        for j in range(0,num-i-1):
            print("*", end =" ")
        print()
tri()
inv_tri()