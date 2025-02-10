# Prime Number

num=int(input("Enter a number "))
factor=0
for den in range(1,num+1):
    if num%den==0:
        factor+=1
if factor==2:
    print('Prime No')
else:
    print("Not Prime No")

