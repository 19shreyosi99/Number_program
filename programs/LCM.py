num1=int(input("enter 1st number"))
num2=int(input("enter 2nd number"))
if num1>num2:
    lcm=num1
else:
    lcm=num2
while True:
    if lcm%num1==0 and lcm%num2==0:
        print(lcm)
        break
    else:
        lcm+=1