

class Node:
    def __init__(self,data): #สร้างnode
        self.data = data  #nodeข้อมูล
        self.next = None #node ถัดไปให้ว่าง

class Linkedlist:
    def __init__(self): #สร้างll
        self.head = None #สร้างหัว list ให้ว่าง
        self.size = 0 #กำหนดลิสไซต์ ให้เป็น 0

    def __str__(self): #ไว้สำหรันรีเทรนค่ากลับ
        s = "" #กำหนดตัวแปรให้ว่างเพื่อไว้เติมข้อมูล
        t = self.head
        while t != None:
            s+=str(t.data)
            t=t.next
            if t != None:
                s+="->"
        return s

    def isEmpty(self): #เช็คเฮดว่าว่างไหม ถ้าว่างให้return none
        return self.head == None

    def append(self,data):#เพิ่ม data ต่อท้าย linked list
        p = Node(data)
        if self.isEmpty():
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t=t.next
            t.next = p
        self.size +=1
    
    def insert(self,index,data): #แทรกข้อมูล
        p = Node(data)
        if self.isEmpty():
            self.head = p
        elif index == 0:
            p.next = self.head
            self.head = p 
        else:
            t = self.head
            i = 0
            while i < index-1:
                i+=1
                t=t.next
            p.next = t.next
            t.next = p
        self.size +=1
    
inp = input("Enter input : ").split(',')
l = inp[0].split()
lli = Linkedlist()

for i in l:lli.append(int(i))
if lli.isEmpty():
    print("List is Empty")
else:
    print("link list : "+lli.__str__())

for i in inp[1:]:
    index,data = [int(j)for j in i.split(":")]
    if index < 0 or index > lli.size:
        print("Data cannot be added")
    else:
        lli.insert(index,data)
        print("index = "+str(index)+ "and data ="+str(data))
    
    if lli.isEmpty():
        print("List is Empty")
    else:
        print("link list : " +lli.__str__())