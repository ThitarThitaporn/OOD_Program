from re import T


def append(self,data):
    p = Node(data)
    if self.isEmpty():
        self.head = p
    else:
        t = self.head
        while t.next!= None:
            t=t.next
        t.next = p

    
def addHead(self,data):
    p = Node(data)
    if self.isEmpty():
        self.head = p
    else:
        t = self.head
        p.next = t 
        t = p


def insert(self,data,index):
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
            t = t.next
        p.next = t.next
        t.next = p
