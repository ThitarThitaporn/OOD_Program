from dataclasses import dataclass


class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root =  None

    def insert(self,data): 
        p = Node(data)
        if self.root == None : #check root 
            self.root = p
            return self.root

        else:
            cur = self.root
            while cur != None:
                if data >= cur.data : #check right upper
                    if cur.right == None:
                        cur.right = p
                        return self.root
                    cur = cur.right

                elif data < cur.data : #check left lower
                    if cur.left == None:
                        cur.left = p
                        return self.root
                    cur = cur.left 

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