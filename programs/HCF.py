num1=int(input("enter 1st number"))
num2=int(input("enter 2nd number"))
if num1>num2:
    hcf=num1
else:
    hcf=num2
while True:
    if num1%hcf==0 and num2%hcf==0:
        print(hcf)
        break
    else:
        hcf-=1