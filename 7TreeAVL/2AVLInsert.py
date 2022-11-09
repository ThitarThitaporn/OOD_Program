class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
    
    def __str__(self):
        return str(self.data)

class AVL:

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def insert(self, root, data):
        if root is None:
            return Node(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        root.height = 1 + max(self.getHeight(root.right), self.getHeight(root.left))
        balance = self.getBalance(root)

        # Left Left 
        if balance > 1 and data < root.left.data:
           # print('Not Balance, Rebalance!') 
            return self.rightR(root) 
        # Right Right 
        if balance < -1 and data >= root.right.data:
            #print('Not Balance, Rebalance!') 
            return self.leftR(root) 

        # Left Right 
        if balance > 1 and data >= root.left.data:
            #print('Not Balance, Rebalance!') 
            root.left = self.leftR(root.left) 
            return self.rightR(root) 

        # Right Left 
        if balance < -1 and data < root.right.data:
            #print('Not Balance, Rebalance!') 
            root.right = self.rightR(root.right) 
            return self.leftR(root) 

        return root

    def leftR(self, n): 
        m = n.right 
        temp = m.left 
        m.left = n 
        n.right = temp
        n.height = 1 + max(self.getHeight(n.left), self.getHeight(n.right)) 
        m.height = 1 + max(self.getHeight(m.left), self.getHeight(m.right)) 
        return m 

    def rightR(self, n): 
        m = n.left 
        temp = m.right 
        m.right = n 
        n.left = temp 
        n.height = 1 + max(self.getHeight(n.left), self.getHeight(n.right)) 
        m.height = 1 + max(self.getHeight(m.left), self.getHeight(m.right)) 
        return m  

    def getHeight(self, root): 
        if not root: 
            return 0
        return root.height 

    def getBalance(self, root): 
        if not root: 
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right) 


inp = list(map(int, input("Enter Input : ").split()))
Tree = AVL()
root = None
for x in inp:
    print(f"Insert : ( {x} )")
    root = Tree.insert(root, x)
    Tree.printTree(root)
    print('--------------------------------------------------')