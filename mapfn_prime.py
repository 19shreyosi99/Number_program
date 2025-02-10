def prime(num):
    for den in range (2,num//2+1):
        if num%den==0:
            return 'Not Prime'
            break
    return 'Prime'
print(list(map(prime,[10,11,12,13,14,15,16,17,18,19,20])))