def nodeat(self,index):
    n=0
    p=self.head
    while p!=None:
        n+=1
        if(n==index):
            return p
        p=p.next
def reverse(self):
    tail=self.tail
    p=self.tail
    n=self.size()-1
    while n!=0 :
        p.next=self.nodeat(n)
        print(p.data,p.next.data)
        p=p.next
        n=n-1
        p.next=None
        self.head=tail
        print(1)
            