def recursiveFun(n):
    if n<1:
        return 
    
    recursiveFun(n-1)
    print(n)
recursiveFun(5)

def fib(n):
    if n<2:
        return n
    else:
        return fib(n-1)+fib(n-2)
for i in range(6):
    print(fib(i))