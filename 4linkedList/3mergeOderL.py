class node:
    def __init__(self,data,next = None ):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

def createList(l=[]): # สำหรับการสร้าง LinkList ที่รับ List เข้ามาโดยจะ return Head ของ Linklist
    head = cur = node(l[0])
    for i in range(1,len(l)):
        cur.next = node(l[i])
        if i < len(l):
            cur = cur.next
    return head

def printList(H): #สำหรับการ print LinkList โดยจะรับค่าเป็น head ของ Linklist และจะทำการ print ทุกตัวที่อยู่ใน Linklist ต่อจาก head จนครบทุกตัว
    s = ""
    while H:
        s  += str(H) + " "
        H = H.next
    print(s)
  

def mergeOrderesList(p,q): #สำหรับการ merge linklist 2 ตัวเข้าด้วยกันโดยให้นำมาต่อกันโดยเรียงตามค่า value โดยที่ให้รับ parameter 2 ตัว และจะ return Head ของ Linklist ที่ทำการ merge แล้ว
    if p.data < q.data:
        head = cur = p
        p = p.next
    else:
        head = cur = q
        q = q.next

    while p or q:
        if p != None and q != None and int(p.data) <= int(q.data):
                cur.next = p
                p = p.next

        elif p != None and q != None and int(p.data) > int(q.data):
                cur.next = q
                q = q.next

        elif p == None and q != None:
                cur.next = q
                q = q.next

        elif p != None and q == None:
                cur.next = p
                p =p.next

        cur = cur.next
    return head
    
inp,L1,L2 = input("Enter 2 Lists : ").split(),[],[]
for i in inp[0].split(','):
    L1.append(i)

for i in inp[1].split(','):
    L2.append(i)
    
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)

'''
Testcase : #1 1
Enter 2 Lists : 1,3,5,7,10,20,22 4,6,7,8,15

Testcase : #2 2
Enter 2 Lists : 1,4,5,5,6,7 2,3,6,9,10

Testcase : #3 3
Enter 2 Lists : 2,2,2,10 1,1,1,1,5,5,5,6,7,8
'''
