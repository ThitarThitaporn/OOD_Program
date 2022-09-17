class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList :

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        new = Node(item)
        if self.isEmpty() :
            self.head = new
            self.tail = new
        else :
            current = self.head
            while current.next != None :
                current = current.next
            current.next = new
            new.previous = self.tail
            self.tail = new

    def size(self):
        current = self.head
        n = 0
        while current :
            current = current.next
            n += 1
        return n

L1=LinkedList()
L2=LinkedList()

input = input("Enter Input (L1,L2) : ").split(" ")

inputL1 = input[0].split("->")
for data in inputL1 :
    L1.append(data)
print("L1    :",L1)

inputL2 = input[1].split("->")
for data in inputL2 :
    L2.append(data)
print("L2    :",L2)

if not L2.isEmpty() :
    current = L2.tail
    while current != None :
        L1.append(current.value)
        current = current.previous

print(f'Merge : {L1}')