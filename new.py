def factorial(n):
    if n <=1:
        return 1
    fac = 1
    for i in range(1,n+1):
        fac*=i
    return fac
a=factorial(10)
print(a)