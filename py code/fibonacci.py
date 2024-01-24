num=20

a=0
b =1
c=0
print("Fibo is: ", end="")
for i in range(0,num):
    print(c," ", end="")
    c=a+b
    a=b
    b=c