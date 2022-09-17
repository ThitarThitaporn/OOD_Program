
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedlist :
    def __init__ (self):  #สำหรับสร้าง linked list
        self.head = None
        self.tail = None
        self.size = 0

    def __str__ (self): #return string แสดง ค่าใน linked list
        s = ""
        if self.isEmty():
            return ""
        cur = self.head.next

        while cur.next != self.tail:
            s += str(cur.data) + "->"
            cur = cur.next
        s += str(cur.data)
        return s

    def str_reverse(self): #return string แสดง ค่าใน linked list จากหลังมาหน้า
        s = ""
        if self.isEmpty():
            return ""
        cur = self.tail.prev

        while cur.prev != self.head :
            s += str(cur.data) + "->"
            cur = cur.prev
        s -= str(cur.data)
        return s

    def isEmpty(self): #return list นั้นว่างหรือไม่
        return self.head.next == self.tail

    def append(self,data): #add node ที่มี data เป็น parameter ข้างท้าย linked list
        p = Node(data)
        p.next = self.tail
        p.prev = self.tail.prev
        self.tail.prev.next = p
        self.tail.prev = p

inp = input('Enter Input : ')
inp=inp.replace(', ',',').split(',')
DL= DoublyLL()
for i in inp:
    i = i.split()
    if i[0] == 'A':
        DL.append(i[1])
        print(f"linked list : {DL}")
        print(f"reverse : {DL.str_reverse()}")
    elif i[0] == 'Ab':
        DL.insert(0, i[1])
        print(f"linked list : {DL}")
        print(f"reverse : {DL.str_reverse()}")
    elif i[0] == 'I':
        ele = i[1].split(':')
        if int(ele[0])<0 or int(ele[0])>DL.size:
            print("Data cannot be added")
        else:
            DL.insert(int(ele[0]), ele[1])
            print(f"index = {ele[0]} and data = {ele[1]}")
        print(f"linked list : {DL}")
        print(f"reverse : {DL.str_reverse()}")   

    elif i[0] == 'R':
        a = DL.remove(i[1])
        if a[0] == None:
             print("Not Found!")
        else:
            print(f"removed : {a[0].data} from index : {a[1]}")
        print(f"linked list : {DL}")
        print(f"reverse : {DL.str_reverse()}")  


