def prime(num,den=1,fa_count=0):
    if den>num:
        return fa_count==2
    if num%den==0:
        fa_count+=1
    return prime(num,den+1,fa_count)
num=int(input('enter a number'))
print("Prime" if prime(num) else 'Not Prime')