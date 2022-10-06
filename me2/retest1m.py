class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur,s = self.head ,str(self.head.value) + " "
        while cur.next!=None:
            s+=str(cur.next.value) + ""
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self,data):
        p = Node(data)
        if self.isEmpty():
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t =t.next
            t.next = p

    def addHead(self,item):
        p = Node(item)
        if self.isEmpty():
            self.head = p
        else:
            t = self.head
            p.next = t
            t = p

    def search(self,item):
        t = self.head
        if t != None:
            while t.value != item:
                if t.next == None and t.value != item:
                    return "Not Found"
                else:
                    t = t.next
            return "Found"

        else:
            return "Not Found"
            

    def index(self,item):
         t = self.head 
         index = 0
         if t != None:
            while t.value != item:
                if t.value == None and t.value != item:
                    return '-1'
                else:
                    t = t.next
                    index += 1
            return index

         else:
            return '-1'

    def size(self):
        t= self.head
        count = 0
        if t!=None:
            while t != None:
                count +=1
                t = t.next
        return count

    def pop(self,item):
        t = self.head
        count = 0
        if item == 0 and t!= None:
            t = None
            return "success"
        while t!= None:
            if count== int(item)-1:
                if t.next == None:
                    return " out of range"

                elif t.next.next == None:
                    t.next = None
                    return "success"
                elif t.next.next != None:
                    t.next = t.next.next
                    return "success"
            count +=1
            t  = t.next
        return "out of range"

L = Linkedlist()
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
