def print1ToN(n): #ฟังก์ชั่นที่แสดงผลเลข 1 จนถึง n
    if n <= 0:
        print('1',end=' ')
    else:
        if n-1 > 0: #วนโดยการเรียกใช้ฟังก์ชันไปเรื่อยๆแล้วปริ้น
            print1ToN(n-1) #จุดวน
        print(n,end=' ')

def printNto1(n): #ฟังก์ชั่นที่แสดงผลเลขตั้งแต่ n จนถึง 1
    if n <= 0 :
        print('1',end='')
    else : #ปริ้นก่อนแล้วค่อยวนฟังก์ชัน
        print(n,end=' ')
        if n-1 > 0 :
            printNto1(n-1) #จุดวน
        
n = int(input("Enter Input : "))

print1ToN(n)
printNto1(n)