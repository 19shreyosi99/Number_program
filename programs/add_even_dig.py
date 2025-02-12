num=int(input("enter a number"))
res=1
while num!=0:
    rem=num%10
    if rem%2==0:
        res+=rem
    num//=10
print(res)
