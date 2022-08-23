'''ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ STACK ในการแก้ปัญหา



A  <value>  ให้นำ value ไปใส่ใน STACK และทำการแสดงผล Size ปัจจุบันของ STACK

P                 ให้ทำการแสดงผลของvalueที่อยู่ท้ายสุดและindexของvalueนั้นจากนั้นทำการ Pop_Stack ถ้าหากไม่มี value อยู่ใน Stack ให้แสดงผลเป็น  -1

*** ในตอนสุดท้ยถ้าหากใน Stack ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty'''

class Stack():
    def __init__(self):
        self.items = []
        
    def push(self,num):
        self.items.append(int(num))
        self.items.sort()
        self.size = len(self.items)
        return f'Add = {num} and Size = {self.size} '
    
    def pop(self):
        self.size = len(self.items)-(1)
        if self.items == []:
            print('-1')
            return -1
        else:
            print(f"Pop = {self.items[-1]} and Index = {self.size}")
        self.items.pop()
     
st = Stack()
S = input("Enter Input : ").split(',')
for i in range(len(S)):
    try:
        key, num = S[i].split()
        #print(key,num)
    except:
        key = S[i][0]
    if key == 'A':
        print(st.push(num))
    elif key == 'P':
        st.pop()

if st.items == []:
    print('Value in Stack = Empty')
else :
    print('Value in Stack =' ,*st.items)