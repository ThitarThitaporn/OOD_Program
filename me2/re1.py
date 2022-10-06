def print1toN(n):
    if n<0:
        print("1",end=' ')
    else:
        if n-1> 0:
            print1toN(n-1)
        print(n,end=' ')

def printNto1(n):
    if n<0:
        print("1",end=' ')
    else:
        print(n,end=' ')
        if n-1>0:
            printNto1(n-1)

n = int(input("enter number : "))
print1toN(n)
printNto1(n)