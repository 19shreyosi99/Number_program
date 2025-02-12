num=int(input("enter a number"))
dig=len(str(num))
pow=10**(dig-1)
res=0

while num!=0:
    rem=num%10
    res=res+rem*pow
    pow //= 10
    num//=10
print(res)