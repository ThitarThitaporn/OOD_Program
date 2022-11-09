from ast import Global


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data) #error1 T-T

class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        p = Node(data)
        if self.root == None :
            self.root = p
            return self.root

        else:
            cur = self.root
            while cur != None:
                if data >= cur.data: #check data ที่มากกว่า (right) 
                    if cur.right == None:
                        cur.right = Node(data)
                        return self.root
                    cur = cur.right

                elif data < cur.data : #check data ที่น้อย (left) 
                    if cur.left == None:
                        cur.left = Node(data)
                        return self.root
                    cur = cur.left
                

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
    def min(self,data):
            global min
            if data < min:
                min = data
            return min

    def max(self,data):
            global max
            if data > max:
                max = data
            return max

T = BST()
min = 99999
max = -99999
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
    T.min(i)
    T.max(i)

T.printTree(root)
print('--------------------------------------------------')
print(f'min : {min}')
print(f'max : {max}')