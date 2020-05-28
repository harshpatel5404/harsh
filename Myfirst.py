def genfib(n):
    a,b=0,1
    while(n!=0):
        yield a
        a,b=b,a+b
        n-=1
f=genfibo(7)
for i in f:
    print(i)
