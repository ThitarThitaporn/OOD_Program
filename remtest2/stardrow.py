def draw(inp,i) :
    line = int((i/(inp-1))+1)
    n = i%(inp-1)

    if n==0 :
        if i==(inp-1):
            print("#")
        else :
            print("^") 
    elif n<=inp-line :
        print("^",end="")
    elif inp-line < n <= (inp-line)+(line-1) :
        print("#",end="")
    else :
        print("^",end="")


    if i == (inp-1)*inp :
        return
    else :
        draw(inp,i+1)


inp = input("input = ")
inp = int(inp)
draw(inp,1)