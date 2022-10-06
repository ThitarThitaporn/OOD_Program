def gcd(a,b):
    if b == 0:
        return abs(a)
    else:
        return gcd(b, a%b)

inp = input('Enter Input : ').split()
if int(inp[0]) == 0 and int(inp[1]) == 0:
    print('Error! must be not all zero.')
else:
    print(f'The gcd of {max(inp)} and {min(inp)} is : {gcd(int(max(inp)),int(min(inp)))}')
