a = "eye"
c = []
x=len(a)
for i in range(1,x+1):
     c.append(a[x-i])

d = []

d = list(reversed(c))
if d==c:
    print("it is palindrome")
else:
     print("It is not palindrome")