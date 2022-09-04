class Queue:
    def __init__(self, l=None):
        if l != None:
            self.items = l
        else:
            self.items = []

    def enqueue(self, e):
        self.items.append(e)

    def dequeue(self):
        if len(self.items) == 0:
            return None
        return self.items.pop(0)

input = input("Enter Input : ").split("/")
m = input[0]
n = input[1].split(",")

book = Queue(m.split(" "))
for i in n:
    if i == "D":
        book.dequeue()
    else:
        e = i.split(" ")[1]
        book.enqueue(e)

seen = {}
check = book.items
isDup = False
for c in check:
    if c in seen:
        isDup = True
        break
    else:
        seen[c] = 1
if not isDup:
    print("NO Duplicate")
else:
    print("Duplicate")