def prime(num,factor=0):
    for den in range(1,num+1):
        if num%den==0:
            factor+=1
    return factor==2
num=int(input("Enter a number"))
print('Prime' if prime(num) else 'Not Prime')

