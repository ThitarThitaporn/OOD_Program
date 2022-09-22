def length(txt): 
    if txt == '': 
        return 0
    else:
        num = length(txt[:-1]) 
        if num%2==0 :
            print(txt[num],end='*')
        else:
            print(txt[num],end='~')

        return num+1
print('\n',length(input("Enter Input : ")),sep="")
