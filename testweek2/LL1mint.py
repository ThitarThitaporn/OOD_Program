class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        # add at the end of list
        p = Node(item)
        if self.head == None: #null list
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p

    def addHead(self, item):
        p = Node(item)
        if self.head == None: #null list
            self.head = p
        else:
            p.next = self.head
            self.head = p
            
    def search(self, item):
        p = self.head
        if self.head != None:
            while p.value != item:
                if p.next == None and p.value != item:
                    return 'Not Found'
                else:
                    p = p.next
            return "Found"
        else:
            return 'Not Found'
                
    def index(self, item):
        p = self.head
        index = 0
        if self.head != None:
            while p.value != item:
                if p.next == None and p.value != item:
                    return '-1'
                else:
                    p = p.next
                    index += 1
            return index
        else:
            return '-1'

    def size(self):
        p = self.head
        count = 0
        if not self.head == None: #null list
            while p != None:
                count += 1
                p = p.next
        return count

    def pop(self, item):
        p = self.head
        count = 0
        if item == 0 and p != None: #pop head
            self.head = None
            return "Success"
        while p != None:
            if count == int(item)-1:
                if p.next == None:
                    return "Out of Range"
                elif p.next.next == None:
                    p.next = None
                    return "Success"
                elif p.next.next != None:
                    p.next = p.next.next
                    return "Success"
            count += 1
            p = p.next
        return "Out of Range"

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)