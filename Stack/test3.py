from pickle import DUP


class StackCalc:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[-1]

    def push(self,tmp):
        self.items.append(tmp)
    
    def pop(self):
        return self.items.pop()

def run(st):
    s = StackCalc()
    for i in st:
        if i=="+":s.push(s.pop()+s.pop())
        elif i=="-":s.push(-1*s.pop()+s.pop())
        elif i=="*":s.push(s.pop()*s.pop())
        elif i=="/":
            a=s.pop()
            b=s.pop()
            s.push(b/a)

        elif i== 'DUP' :
            s.peek(i)
           #print ('1')
        elif i== 'POP' :
            s.pop(i)
        elif i== 'PSH' :
            s.push(i)

        else:
           s.push()
           
    return s.pop()

print("* Stack Calculator *")
arg = list(input("Enter arguments : ").split())
print(int(run(arg)))