num=[1,2,3,4,5,6,7,8,9]
Sqr_num=[]
for number in num:
    Sqr_num.append(number**2)
print(Sqr_num)

print("x"*30)

Sqr_num2=[number2**2 for number2 in num]
print(Sqr_num2)