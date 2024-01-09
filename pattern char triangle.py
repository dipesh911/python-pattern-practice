num=6

for i in range(1,num+1):
    a = 65
    for j in range(0,num-i):
        print(" ", end="")
    for j in range(0,i):
        print(chr(a), end = "")
        a += 1
    a = a -2
    for j in range(0,i-1):
        print(chr(a), end="")
        a -= 1
    print()
