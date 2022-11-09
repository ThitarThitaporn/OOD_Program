class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.data)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        p = Node(value)
        if self.root == None :
            self.root = p
            return self.root

        else:
            cur = self.root
            while cur != None:
                if value >= cur.data:
                    if cur.right == None:
                        cur.right = p
                        return self.root
                    cur = cur.right
                elif value < cur.data :
                    if cur.left == None:
                        cur.left = p
                        return self.root
                    cur = cur.left


    def delete(self,r,data):
        if r == None: 
            print("Error! Not Found DATA")
            return

        if self.root.left == None and self.root.right == None and self.root.data == data:
            self.root = None
        elif self.root.left == None and self.root.data == data:
            self.root = self.root.right
        elif self.root.right == None and self.root.data == data:
            self.root = self.root.left

        if r.data != data :
            if r.data > data :
                r.left = self.delete(r.left, data)
            elif r.data < data :
                r.right = self.delete(r.right, data) 
        elif r.data == data :
            if r.left == None :
                r = r.right
                return r
            elif r.right == None :
                r = r.left
                return r
            else:
                cur = r.right
                while cur.left != None :
                    cur = cur.left
                r.data = cur.data 
                r.right = self.delete(r.right, cur.data)

        return r

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level +1 )
        print('     ' * level, node)
        printTree90(node.left, level +1 )

tree = BinarySearchTree()
data = input("Enter Input : ").split(",")

for i in data :
    inp = i.split(" ")
    if inp[0] == 'i' :
        tree.insert(int(inp[1]))
        print(f'insert {inp[1]}')
        printTree90(tree.root)
    elif inp[0] == 'd' :
        print(f'delete {inp[1]}')
        tree.delete(tree.root,int(inp[1]))
        printTree90(tree.root)