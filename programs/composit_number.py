num=int(input("enter a number"))
factor=0
for val in range(1,num+1):
    if num%val==0:
        factor+=1
if factor>2:
    print("composit number")
else:
    print("not composit")
