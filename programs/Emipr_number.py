num=14
copy=num
rev=0
while num!=0:
    rem=num%10
    rev=rev*10+rem
    num//=10
if copy!=rev:
    for den in range(2,copy//2+1):
        if copy%den==0:
            print('not prime')
            break
    else:
        for den in range(2,rev//2+1):
            if rev%den==0:
                print('prime not')
                break
        else:
            print('Emirp')
else:
    print('not')