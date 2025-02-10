def factorial(num,fact=1):
    for den in range(1,num+1):
        fact *= den
    return fact
num=int(input("Enter a Number"))
print(factorial(num))