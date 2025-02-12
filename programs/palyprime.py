num=int(input("enter a number"))
for val in range(2,num//2+1):
    if num%val==0:
        print("not prime")
        break
    else:
        rev=0
        copy=num
        while num!=0:
            rem=num%10
            rev=rem+rev*10
            num//=10
        if copy==rev:
            print("pallyprime no")
        else:
            print("not palyndrom")
