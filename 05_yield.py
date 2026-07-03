def printFun(n):
    num=0
    for i in range(n+1):
        num=i
    return num
def printfun(n):
    num=0
    for i in range(n+1):
        num=i
    yield num
print(printFun(5))
print(printfun(5))

