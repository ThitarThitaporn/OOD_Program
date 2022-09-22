def length(txt):
    if txt=='':
        return 0
    else:
        num = length(txt[:-1]) 
        print(txt[num],end='*' if num%2==0 else "~") #ใส่ if else ข้างหลัง เพื่อเปลี่ยนแค่ * ~
        return num+1

print("\n",length(input("Enter Input : ")),sep="")