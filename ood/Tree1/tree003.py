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

    def insert(self, data):
        if self.root == None:
            NewNode = Node(data)
            self.root = NewNode
        else:
            NewNode = Node(data)
            nowNode = self.root
            while (nowNode.right != None or nowNode.left != None):
                if (data < nowNode.data and nowNode.left != None):
                    nowNode = nowNode.left
                elif (data > nowNode.data and nowNode.right != None):
                    nowNode = nowNode.right
                else:
                    break
                    
            if (data < nowNode.data):
                nowNode.left = NewNode
            elif (data > nowNode.data):
                nowNode.right = NewNode
        return self.root

    def findDepth(self, node, key, depth = 0):
        nowNode = node
        if node.data == key:
            return 0
        while (nowNode != None):
            if (nowNode != None and key < nowNode.data):
                nowNode = nowNode.left
            elif (nowNode != None and key > nowNode.data):
                nowNode = nowNode.right
            depth += 1
            if (nowNode != None and key == nowNode.data):
                return depth
        return -1
        

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


    def sumofrange(self , node , min , max):
        if (node == None):
            return 0
        sum = 0
        if (node.data <= max and node.data >= min):
            sum += node.data
        if (node.data < max):
            sum += self.sumofrange(node.right , min , max)
        if (node.data > min):
            sum += self.sumofrange(node.left , min , max)
        return sum

#T = BST()
#inp = [int(i) for i in input('Enter Input : ').split()]
#values = inp[:-1]
#key = inp[-1]
#for i in values:
#    root = T.insert(i)
#T.printTree(root)
#print('-' * 50)
#print(f"Depth of {key} : {T.findDepth(root, key)}")
print("***Range Sum***")
T = BST()
inp = [str(i) for i in input('Enter Input : ').split()]
val = [int(i) for i in inp[:-4]]
minval = int(inp[-3])
maxval = int(inp[-1])
print("\nBinary Search Tree:")
for i in val:
    T.insert(i)
T.printTree(T.root)
print(f"\nRange : [{minval}, {maxval}]")
print(f"Sum of nodes in range = {T.sumofrange(T.root,minval,maxval)}")