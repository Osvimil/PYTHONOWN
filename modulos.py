def suma():
    a = int(input('numero 1'))
    b = int(input('numero 2'))
    print (a+b)

def resta():
    a = int(input('numero 1'))
    b = int(input('numero 2'))
    print (a-b)

def mul():
    a = int(input('numero 1'))
    b = int(input('numero 2'))
    print (a*b)
def div():
    a = int(input('numero 1'))
    b = int(input('numero 2'))
    print (a/b)

def fib(n):
    x,y= 0,1
    while x < n:
        print(x)
        x,y = y, x+y
    print()
