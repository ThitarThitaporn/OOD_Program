class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SingyLinkedlist:
    def __init__ (self):
        self.head =None
        self.size = 0

    def __str__(self):
        s = ""
        t = self.head
        while t != None:
            s += str(t.data)
            t = t.next
            if t != None:
                s += "->"
        return s

    def isEmpty(self):
        return self.head == None

    def append(self,data):
        p = Node(data)
        if self.isEmpty(): #ถ้าว่างให้ใส่ก้อนโนดไปเลย
            self.head = p
        else: #ถ้าไม่ให้เช็คไปเรื่อยๆ
            t = self.head
            while t.next != None : #ไม่ว่าง
                t = t.next
            t.next = p
        self.size+=1
        
    def insert(self,index,data): #ใช้สำหรับการแทรก | index คือ position
        p = Node(data)
        if self.isEmpty() :
            self.head = p
        elif index == 0 :
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
lli = SingyLinkedlist()

for i in l:lli.append(int(i))
if lli.isEmpty():
    print("List is empty")
else:
    print("link list : "+lli.__str__())

for i in inp[1:]:
    index,data = [int(j)for j in i.split(":")]
    if index < 0 or index > lli.size:
        print("Data cannot be added")
    else:
        lli.insert(index,data)
        print("index = "+str(index)+" and data = "+str(data))
        
    if lli.isEmpty():
        print("List is empty")
    else:
        print("link list : "+lli.__str__())