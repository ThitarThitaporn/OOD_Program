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

input = input("Enter Input : ").split(",")

myQueue = Queue()
yourQueue = Queue()

for i in range(len(input)) :
    my,your = input[i].split(" ")
    myQueue.enQueue(str(my))
    yourQueue.enQueue(str(your))

print("My   Queue =",myQueue)
print("Your Queue =",yourQueue)

activity = {
    "0":"Eat",
    "1":"Game",
    "2":"Learn",
    "3":"Movie",
}

location = {
    "0":"Res.",
    "1":"ClassR.",
    "2":"SuperM.",
    "3":"Home",
}

point = 0

for i in range(myQueue.size()) :
    myFirstQ, yourFirstQ = myQueue.deQueue(), yourQueue.deQueue()
    myText = f'{activity[myFirstQ[0]]}:{location[myFirstQ[2]]}'
    yourText = f'{activity[yourFirstQ[0]]}:{location[yourFirstQ[2]]}'

    if myFirstQ[0] == yourFirstQ[0] and myFirstQ[2] != yourFirstQ[2] :
        point += 1
    elif myFirstQ[0] != yourFirstQ[0] and myFirstQ[2] == yourFirstQ[2] :
        point += 2
    elif myFirstQ[0] == yourFirstQ[0] and myFirstQ[2] == yourFirstQ[2] :
        point += 4
    elif myFirstQ[0] != yourFirstQ[0] and myFirstQ[2] != yourFirstQ[2] :
        point -= 5

    myQueue.enQueue(myText)
    yourQueue.enQueue(yourText)

print("My   Activity:Location =",myQueue)
print("Your Activity:Location =",yourQueue)

if point >= 7 :
    print("Yes! You're my love! : Score is " + str(point) + ".")
elif point < 7 and point > 0 :
    print("Umm.. It's complicated relationship! : Score is " + str(point) + ".")
else :
    print("No! We're just friends. : Score is " + str(point) + ".")