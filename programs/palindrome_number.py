num=int(input("enter a number"))
rev=0
copy=num
while num!=0:
    rem=num%10
    rev=rem+rev*10
    num//=10
print('palindrom' if rev==copy else 'not palindrom')
