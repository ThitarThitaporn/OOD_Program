class Stack:
    def __init__(self) :
        self.items = []

    def push(self,i) :
        self.items.append(i)

    def pop(self) :
        return self.items.pop(-1)

    def top(self) :
        return self.items[-1]

    def isEmpty(self) :
        return len(self.items) == 0

    def size(self) :
        return len(self.items)
    
    def reverse(self) :
        self.items.reverse()

    def __str__(self) :
        return "".join(self.items)

class Queue :
    def __init__(self) :
        self.q=[]

    def enQueue(self,i) :
        self.q.append(i)

    def deQueue(self) :
        return self.q.pop(0)

    def isEmpty(self) :
        return len(self.q) == 0

    def size(self) :
        return len(self.q)

    def __str__(self) :
        return ", ".join(self.q)

normal,mirror = input(" Enter Input (Normal, Mirror) : ").split(" ")

sNormal = Stack()
sMirror = Stack()
q = Queue()

bombMirror, bombNormal = 0, 0
failedInter = 0

mirror = mirror[::-1]

for i in mirror :
    if sMirror.size() < 2 :
        sMirror.push(i)
    else :
        sMirror.push(i)
        first = sMirror.pop()
        second = sMirror.pop()
        third = sMirror.pop()
        if first == second and second == third :
            q.enQueue(first)
            bombMirror += 1
        else :
            sMirror.push(third)
            sMirror.push(second)
            sMirror.push(first)

countBomb = 0

for i in normal :
    if sNormal.size() < 2 :
        if sNormal.size() == 1 and i == sNormal.top() :
            countBomb = 2
        else :
            countBomb = 0
        sNormal.push(i)
    else :
        first = sNormal.pop()
        second = sNormal.pop()
        if (first == second or countBomb == 2) and not q.isEmpty():
            countBomb = 0
            interrupt = ""
            interrupt = q.deQueue()
            if interrupt == first == second :
                failedInter += 1
            else :
                sNormal.push(second)
                sNormal.push(first)
                sNormal.push(interrupt)
            sNormal.push(i)
        else :
            sNormal.push(i)
            third = sNormal.pop()
            if first == second == third :
                bombNormal += 1
            else :
                sNormal.push(second)
                sNormal.push(first)
                sNormal.push(third)

print("NORMAL :")
print(sNormal.size())
if sNormal.isEmpty() :
    print("Empty")
else :
    sNormal.reverse()
    print(sNormal)
print(str(bombNormal) + " Explosive(s) ! ! ! (NORMAL)")
if failedInter != 0 :
    print("Failed Interrupted " + str(failedInter) + " Bomb(s)")
print("------------MIRROR------------")
print(": RORRIM")
print(sMirror.size())
if sMirror.isEmpty() :
    print("ytpmE")
else :
    sMirror.reverse()
    print(sMirror)
print("(RORRIM) ! ! ! (s)evisolpxE " + str(bombMirror))