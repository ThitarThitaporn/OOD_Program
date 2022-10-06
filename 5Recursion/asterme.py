def aster(astr,i):
    if i == len(astr):
        return astr
    elif i == 0:
        return aster(astr,i+1)

    elif astr[i]<0 and astr[i-1]>0:
        if abs(astr[i])<astr[i-1]:
            astr.pop(i)

        elif abs(astr[i])>astr[i-1]:
            astr.pop(i-1)

        else:
            astr.pop(i)
            astr.pop(i-1)
        return aster(astr,0)

    else :
        return aster(astr,i+1)

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(aster(x,0))