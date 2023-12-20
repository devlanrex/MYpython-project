def add (a,b):
    ''' Parameters
    a (int): the first parameter
    b(int): the second parameter
    return
    int:sum of a and b '''
    return a+b
x=5
y=6
result = add(x,y)
print(result)


def add(*args):
    sum=0
    for i in args:
        sum +=i
        return sum
result=add(6,7,2)
print(result)