def fibo(n,a=0,b=1):
    if n!=0:
        print(a)
        fibo(n-1,b,a+b)
fibo(10)