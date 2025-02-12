num=int(input("enter a number"))
ans=0
dup=num
while num!=0:
    rem=num%10
    fact=1
    for val in range(1,rem+1):
        fact*=val
    ans+=fact
    num//=10
if dup==ans:
    print('strong number')
else:
    print('not a strong number')