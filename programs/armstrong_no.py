num=int(input("enter a number"))
pow=len(str(num))
res=0
copy=num
while num!=0:
    rem=num%10
    res=res+rem**pow
    num//=10
print('Armstrong Number'if res==copy else "Not Armstrong Number")