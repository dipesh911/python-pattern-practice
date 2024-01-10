num=8

def upper_pattern():
 for i in range(0,num):
     for j in range(0,num-i):
         print("*",end="")
     for k in range(i*2):
         print(" ",end="")
     for l in range(0,num-i):
         print("*",end="")
     print()

def lower_pattern():
   for i in range(1,num+1):
      for j in range(0,i):
         print("*",end = "")
      for k in range(0,2*(num)-2*i):
         print(" ",end = "")
      for l in range(0,i):
         print("*",end = "")
      print()

upper_pattern()
lower_pattern()

