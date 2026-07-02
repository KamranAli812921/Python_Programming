def recursiveFun(n):
    if n<=1:
        return 
    else:
        recursiveFun(n-1)
        print(n)
recursiveFun(5)