
def gcd(a,b):
    if b == 0:
        return abs(a)
    else:
        return gcd(b,b%a)

inp = input("enter number : ").split()
if int(inp[0]) == 0 and inp[1]==0:
    print("error ")
else:
    print(f"the gce of {max(inp)} and {min(inp)} is :{gcd(int(max(inp)),int(min(inp)))}")
