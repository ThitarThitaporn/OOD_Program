class Stack:
    def __init__(self, list1=[]):
        if list1 == None:
            self.items = []
        else:
            self.items = list1

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]
def check(Max):
    i=1;
    st=Stack([S.peek()])
    stc=Stack([])

    while(not S.isEmpty()):
        if(int(Max)<int(S.peek())):
            i+=1
            Max=S.peek()
        st.push(S.peek())
        S.pop()
    while(not st.isEmpty()):
        stc.push(st.pop())

    return i ,stc
def Hed():
    st=Stack([])
    stc=Stack([])
    while(not S.isEmpty()):
       if(int(S.peek())%2==1 ):
        st.push(int(S.pop())+2)
       elif(int(S.peek())%2==0 ):
        st.push(int(S.pop())-1)
      
    while(not st.isEmpty()): 
     
        stc.push(st.pop())    
    return stc

S = Stack([])

inp = input('Enter Input : ').split(',')
for i in inp:
    if(i[0]=='A'):
        i = i.replace('A ','')
        S.push(i)
    elif(i[0]=='B'):
        if(S.isEmpty()):
            print(0)
        else:
           n,S=check(S.peek())
           print(n)
    elif(i[0]=='S'):   
        S=Hed()
       
           