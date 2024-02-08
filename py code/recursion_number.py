
def f(i,n):
    if (i>n):
        return
    print(i)
    i+=1
    f(i,n)

f(1,5)
