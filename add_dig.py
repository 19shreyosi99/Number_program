num=int(input("enter a number"))
res=0
while num!=0:
    rem=num%10
    res+=rem
    num//=10
print(res)