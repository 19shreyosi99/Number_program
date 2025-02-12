num=10110
pow=0
res=0
while num!=0:
    rem=num%10
    res=res+rem*(2**pow)
    pow=pow+1
    num//=10
print(res)