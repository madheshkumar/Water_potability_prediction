n=int(input("enter no. of iterations: "))
x=0
y=1
for i in range(0,n):
    print(x)
    z=x+y
    x=y
    y=z
