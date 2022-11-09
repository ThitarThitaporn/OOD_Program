class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newData = Node(data)
        if self.root is None :
            self.root = newData
        else :
            cur = self.root
            while True :
                if cur.data > data :
                    if cur.left is None :
                        cur.left = newData
                        break
                    else :
                        cur = cur.left
                elif cur.data <= data :
                    if cur.right is None :
                        cur.right = newData
                        break
                    else :
                        cur = cur.right
        return self.root
    
    def printTree(self, node, level = 0) :
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def infix(self, root) :
        if root == None :
            return ""
        elif root.right == None and root.left == None:
            return str(root.data)
        return '(' + self.infix(root.left) + str(root.data) + self.infix(root.right) + ')'

    def prefix(self, root) :
        prefix = ''
        if root == None :
            return ''
        prefix += str(root.data)
        prefix += self.prefix(root.left)
        prefix += self.prefix(root.right)
        return prefix

inp = input("Enter Postfix : ")

s = []
t = BST()

for i in inp :
    if i in '+-*/' :
        x = s.pop()
        y = s.pop()
        s.append(Node(i,y,x))
    else :
        s.append(Node(i))

print("Tree :")
root = s.pop()
t.printTree(root)
print("--------------------------------------------------")
print(f'Infix : {t.infix(root)}')
print(f'Prefix : {t.prefix(root)}')