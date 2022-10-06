from re import T


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def isEmpty(self):
    return self.head == None
def append(self,data):
    p = Node(data)
    if self.isEmpty():
        self.head = p
    else:
        t = self.head
        while t.next != None:
            t=t.next
        t.next = p

# ถ้า self empty ให้หัว เท่ากับโนดเลย 
# อื่นๆ ถ้าหัวต่อไป ไม่ว่าง ให้หัวเท่ากับหัวต่อไป ถ้าว่างให้หัวต่อไปเป็น เป็นโนด

def append(self,data):
    p = Node(data)
    if self.Empty():
        self.head = p

    else:
        t = self.head
        while t.next != None:
            t = t.next
        t.next = p

    
def addHead(self,data):
    p = Node(data)
    if self.isEmpty():
        self.head =p
    else:
        t = self.head
        p.next = t
        t = p

# ถ้า self empty ให้หัว เท่ากับโนดเลย 
# อื่นๆ ให้โนดตัวต่อไป = หัว | หัวเลยกลายเป็นโนด

def addHead(self,data):
    p = Node(data)
    if self.isEmpty():
        self.head = p
    else :
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


# ถ้า self empty ให้หัว เท่ากับโนดเลย 
# ถ้า ตน.=0 ให้โนดตัวต่อไป = หัว | หัวเลยกลายเป็นโนด
#อื่นๆ มี ตัวนับ เริ่มต้น = 0 ขณะที่ ตัวนับ < ตน.-1 ให้ ตัวนับ +1  และ หัว เท่ากับหัวต่อไป
    #โนดต่อไป เท่ากับหัวต่อไป | หัวต่อไป เท่ากัน โนด


def insert(self,index,data):
    p = Node(data)
    if self.isEmpty():
        self.head = p
    elif index == 0:
        p.next = self.head
        self.head = p
    else:
        t =self.head
        i = 0
        while i < index -1 :
            i+=1
            t =t.next
        p.next = t.next
        t.next = p




    
    
def append(self,data):
    p = Node(data)
    if self.isEmpty():
        self.head = p

    else:
        t = self.head
        while t.next != None:
            t = t.next
        t.next =p

def addHead(self,data):
    p = Node(data)
    if self.isEmpty():
        self.head = p
    else:
        t = self.head
        p.next = t 
        t = p

def insert(self,data,index):
    p =Node(data)
    if self.isEmpty():
        self.head = p
    elif index ==0:
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