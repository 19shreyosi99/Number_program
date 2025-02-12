num=int(input("enter a number"))
pow=len(str(num))
res=0
copy=num
while num!=0:
    rem=num%10
    res=res+rem**pow
    pow-=1
    num//=10

print('Disarium' if res==copy else 'not Disarium')
