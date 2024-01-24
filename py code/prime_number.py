num = 179

for i in range(2,num):
    n = num%i
    if n==0:
        print("this is not prime number")
        break
    elif i==(num-1):
        print("this is prime number")