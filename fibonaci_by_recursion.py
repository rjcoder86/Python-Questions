def fibo(n,a=0,b=1):
    if n!=0:
        print(a)
        fibo(n-1,b,a+b)
fibo(10)

#without recursion
def fibonaci(n):
    a,b=0,1
    
    for i in range(n):
        print(a)
        a,b=b,a+b
