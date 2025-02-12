num=19
while num>9:
    res=0
    while num!=0:
        rem=num%10
        res=res+rem**2
        num//=10
    num=res
if num==1 or num==7:
    print('Happy number')
else:
    print("Not Happy number")