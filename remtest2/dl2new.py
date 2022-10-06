class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.previous = None
    
class Linkedlist:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.previous = self.head

    def __str__(self):
        cur = self.head
        s =''
        while cur.next != self.tail:
            s += str(cur.next.data)
            if cur.next.next != self.tail:
                s+='->'
            cur = cur.next
        return s

    def reverse_str(self):
        cur = self.tail
        s=''
        while cur.previous != self.head:
            s+= str(cur.previous.data)
            if cur.previous.previous != self.head:
                s='->'
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head.next == self.tail

    def append(self,data):
        new = Node(data)
        cur = self.tail.previous
        
        new.next = self.tail
        cur.next = new 
        self.tail.previous = new
        new.previous = cur

    def add_before(self,data):
        new = Node(data)
        cur = self.head.next

        new.next = cur
        self.head.next = new
        new.previous = self.head
        cur.previous = new

    def insert(self,index,data):
        new = Node(data)
        cur = self.head.next
        count = 0

        while cur != self.tail or index == 0 or index == self.size():
            if count == index:
                new.next = cur
                new.previous = cur.previous
                cur.previous.next = new 
                cur.previous = new
                return f"index= {index} and data = {data}"
            cur = cur.next
            count += 1
        return 'data cannot be added'

    def remove(self,data):
        cur = self.head.next
        count = 0

        while cur != self.tail:
            if cur.data == data:
                cur.previous.next = cur.next
                cur.next.previous = cur.previous
                return f'remove : {data} form index:{count}'
            cur = cur.next
            count +=1
        return 'nont found'

    def size(self):
        cur = self.head.next
        count =0
        while cur != self.tail:
            count+=1
            cur = cur.next
        return count


L = Linkedlist()
inp = input('Enter Input : ').split(',')
for n in inp:
    key, num = n.split()
    if key == 'A':
        L.append(num)
    elif key == 'Ab':
        L.add_before(num)
    elif key == 'I':
        a = num.split(':')
        print(L.insert(int(a[0]),a[1]))
    elif key == 'R':
        print(L.remove(num))
    print("linked list :", L.__str__())
    print("reverse :", L.reverse_str())

    