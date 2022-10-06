
listPerket = []

def perket(index,n,s,b):
    if(index==len(ls1)):
        if(n != 0):
            sum = abs(b-s)
            listPerket.append(sum)
        return
    inp1, inp2 = ls1[index].split(" ") 
    sumS = s * int(inp1)
    sumB = b + int(inp2)
    perket(index + 1, n, s, b)
    perket(index + 1, n + 1, sumS, sumB)

ls1 = [str(e) for e in input("Enter Input : ").split(',')]


perket(0,0,1,0)
print(min(listPerket))