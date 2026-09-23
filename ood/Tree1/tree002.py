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

    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data) 
        elif data > root.data:
            root.right = self.insert(root.right, data)

        return root

    def findDepth(self, node, key, depth = 0):
        if node is None:
            return -1
        if node.data == key:
            return depth

        if key < node.data:
            return self.findDepth(node.left, key, depth + 1)
        else:
            return self.findDepth(node.right, key, depth + 1)

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
            
    def reverseTree(self, node):
        if node != None:
            self.reverseTree(node.right)
            self.reverseTree(node.left)
            temp = node.right
            node.right = node.left
            node.left = temp

    def sumonnintrange(self, node, min_val, max_val):
        if node is None:
            return 0
        
        value = 0
        if min_val <= node.data <= max_val:
            value = node.data
            
        # ใช้คุณสมบัติของ BST เพื่อตัด Branch ที่ไม่จำเป็นออก (ช่วยประมวลผลไวขึ้น)
        nodeleft = 0
        noderight = 0
        
        if node.data > min_val:
            nodeleft = self.sumonnintrange(node.left, min_val, max_val)
        if node.data < max_val:
            noderight = self.sumonnintrange(node.right, min_val, max_val)
            
        return value + nodeleft + noderight

print("***Range Sum***")
# --- ส่วนประมวลผล Input/Output ---
T = BST()
inp = input('Enter input : ').split('/')

raw_nodes = [int(i) for i in inp[0].split()]
min_val = int(inp[1])
max_val = int(inp[2])

root = None
for i in raw_nodes:
    root = T.insert(root, i)
print("")
print("Binary Search Tree:")
T.printTree(root)
print()
print(f"Range : [{min_val}, {max_val}]")
print(f"Sum of nodes in range = {T.sumonnintrange(root, min_val, max_val)}")