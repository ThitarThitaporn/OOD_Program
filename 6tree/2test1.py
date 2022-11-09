class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

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

    def min(self):
        root = self.root
        while root.left:
            root = root.left
        return root.data

    def max(self):
        root = self.root
        while root.right:
            root = root.right
        return root.data

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
print(f"Min : {T.min()}")
print(f"Max : {T.max()}")

