
num = 5

for i in range(1,num+1):
    a = 65
    for j in range(0,i):
        print(chr(a), end = " ")
        a = a + 1
    print()