
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

    def __str__ (self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,item): #เพิ่มข้อมูลต่อท้าย linked list
        p = Node(item)
        if self.head == None:
            self.head = p
        else :
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p
    
    def index(self,id:int):
        count = 0
        t = self.head
        while t.next != None:
            if(id==count):
                break;
            count += 1
            t = t.next
        return str(t.value)

    def showNode(self):
        p = self.head
        while p !=None:
            print(p.value,end='')
            if(p.next != None):
                print('->',end='')
            p = p.next
        print()

    def size(self):
        count = 0
        current_node = self.head
        while(current_node != None):
            count += 1
            current_node = current_node.next
        return count   

    def search(self, item):
        found = False
        current_node = self.head
        while current_node != None :
            if current_node.value == item :
                found = True
                break
            else:
                current_node = current_node.next

    def set_next(self,id1,id2):
        
        c=0
        t=self.head
        n1=Node(None)
        n2=Node(None)
        if(self.size()!=0):
            if(self.size()<id2+1):
                print("index not in length, append :",id2)
                self.append(id2)
                
            elif(self.size()<id1+1):
                print("Error! {index not in length}:",id1)
            else:
                index2=None
                while t != None :
                    if(id1==c):
                        n1=t
                    if(id2==c):
                        n2=t
                        index2=c
                        #print(index2)
                    c+=1
                    t = t.next
                n1.next=n2
                
                print("Set node.next complete!, index:value =",str(id1)+':'+self.index(id1),'->',str(id2)+':'+self.index(id2))
                return n2
        else:
            print("Error! {list is empty}")
        

    def checkLoop(self,n):
        if(self.head==None):
            print("No Loop")
            print("Empty")
            return
        if(n!=None and n.next!=None):
            print("Found Loop")
        else:
            print("No Loop")
            self.showNode()

L1=LinkedList()
inp= input('Enter input : ').split(',')
n=Node(None)
for i in inp:
    if(i[0]=='A'):
        L1.append(i.replace('A ',''))
        L1.showNode()
    else:
        i=i.replace('S ','')
        id=i.split(':')
        n=L1.set_next(int(id[0]),int(id[1]))

L1.checkLoop(n)