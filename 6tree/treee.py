class Node(object):
    def __init__(self, data = None):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self, data):
        if self.data == data:
            return False
        elif data < self.data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

    def minValueNode(self, node):
        current = node
        while(current.left is not None):
            current = current.left
        return current 
    
    def maxValueNode(self, node):
        current = node
        while(current.right is not None):
            current = current.right
        return current     

    def delete(self, data):
        if self is None:
            return None

        if data < self.data:
            self.left = self.left.delete(data)
        elif data > self.data:
            self.right = self.right.delete(data)
        else:
            #delete node with 1 child
            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp
            
            #delelt node with 2 child
            temp = self.minValueNode(self.right)
            self.data = temp.data
            self.right = self.right.delete(temp.data)
        return self

    def find(self, data):
        if data == self.data:
            return True
        elif data < self.data:
            if self.left:
                return self.left.find(data)
            else:
                return False
        else:
            if self.right:
                return self.right.find(data)
            else:
                return False
    
    def preOrder(self):
        #[mid] --> [left] --> [right]
        if self:
            print(str(self.data), end=' ')
            if self.left:
                self.left.preOrder()
            if self.right:
                self.right.preOrder()
    
    def inOrder(self):
        #[left] --> [mid] --> [right]
        if self:
            if self.left:
                self.left.inOrder()
            print(str(self.data), end=' ')
            if self.right:
                self.right.inOrder()
    
    def postOrder(self):
        #[left] --> [right] --> [mid]
        if self:
            if self.left:
                self.left.postOrder()
            if self.right:
                self.right.postOrder()
            print(str(self.data), end=' ')

    def minValue(self, node):
        if self:
            return self.minValueNode(node).data

    def maxValue(self, node):
        if self:
            return self.maxValueNode(node).data    
    
    def height(self, node):
            if node is None:
                return 0
            else:
                leftHeight = node.height(node.left)
                rightHeight = node.height(node.right)

                if leftHeight > rightHeight:
                    return leftHeight + 1
                else:
                    return rightHeight + 1   

class Tree(object):
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
    
    def delete(self,data):
        if self.root is not None:
            return self.root.delete(data)
    
    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False
    
    def preOrder(self):
        if self.root is not None:
            print()
            print('Preorder: ', end='')
            self.root.preOrder()
    
    def inOrder(self):
        if self.root is not None:
            print()
            print('Inorder: ', end='')
            self.root.inOrder()

    def postOrder(self):
        if self.root is not None:
            print()
            print('Postorder: ', end='')
            self.root.postOrder()
    
    def min(self):
        if self.root is not None:
            print()
            print('Min: ', end='')
            return self.root.minValue(self.root)
    
    def max(self):
        if self.root is not None:
            print('Max: ', end='')
            return self.root.maxValue(self.root)  

    def height(self):
        if self.root is not None:
            print('height: ', end='')
            return self.root.height(self.root) - 1


#5 3 6 8 9 10 1
if __name__ == '__main__':
    tree = Tree()
    inp = [int(i) for i in input('Enter Input : ').split()]
    for i in inp:
        root = tree.insert(i)

    tree.preOrder()
    tree.inOrder()
    tree.postOrder()
    print(tree.min())
    print(tree.max())

    print(tree.height())


