def greet(*args):
    for name in args:
        print("Hi! "+name)
   
greet("Kamran","Irfan","Arshad")

def sum(*args):
    sum=0
    for number in args:
        sum+=int(number)
    return sum

print("The of the numbers is : "+str(sum(1,2,3,10,4,5)))
