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
        self.pathtonext = None

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

    def insertcomplete(self, data):
        Newnode = Node(data)
        if self.root == None:
            self.root = Newnode
        else:
            path = self.pathtonext
            nodenow = self.root
            for i in path[:-1]:
                if i == 'L':
                    if nodenow.left:
                        nodenow = nodenow.left
                else:
                    if nodenow.right:
                        nodenow = nodenow.right
            if path[-1] == 'L':
                nodenow.left = Newnode
            else:
                nodenow.right = Newnode
        self.pathtonext = self.getnextpath(self.pathtonext)

    def insertfix(self, data,way):
            Newnode = Node(data)
            if self.root == None:
                self.root = Newnode
            else:
                #print(self.pathtonext)
                nodenow = self.root
                if (way == 'L'):
                    while (nodenow.left != None):
                        nodenow = nodenow.left
                    nodenow.left = Newnode
                else:
                    while (nodenow.right != None):
                        nodenow = nodenow.right
                    nodenow.right = Newnode

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

    def getnextpath(self , str1):
        if (str1 == None):
            return "L"
        idx = len(str1) - 1
        ans = list(str1)
        while (idx >= 0 and str1[idx] == 'R'):
            idx -= 1
        if (idx == -1):
            return ('L'*(len(str1) + 1))
        else:
            ans[idx] = 'R'
            lastidx = len(str1) - 1
            idx += 1
            while (idx <= lastidx):
                ans[idx] = 'L'
                idx += 1
            return "".join(ans)

    def dupwayfix(self , node):
        if (node == None):
            return
        self.insertfix(node.data,'R')
        self.dupwayfix(node.left)
        self.dupwayfix(node.right)

#T = BST()
#inp = [int(i) for i in input('Enter Input : ').split()]
#values = inp[:-1]
#key = inp[-1]
#for i in values:
#    root = T.insert(i)
#T.printTree(root)
#print('-' * 50)
#print(f"Depth of {key} : {T.findDepth(root, key)}")



#print("***Range Sum***")
#T = BST()
#inp = [str(i) for i in input('Enter Input : ').split()]
#val = [int(i) for i in inp[:-4]]
#minval = int(inp[-3])
#maxval = int(inp[-1])
#print("\nBinary Search Tree:")
#for i in val:
#    T.insert(i)
#T.printTree(T.root)
#print(f"\nRange : [{minval}, {maxval}]")
#print(f"Sum of nodes in range = {T.sumofrange(T.root,minval,maxval)}")

#word_list = ['L', 'R', 'LL', 'LR', 'RL', 'RR', 'LLL', 'LLR', 'LRL']
#for v in word_list:
#    print(f"{v} : {T.getnextpath(v)}")

T = BST()
inp = [int(i) for i in input('Enter Binary Tree : ').split()]
for i in inp:
    T.insertcomplete(i)
print("Before:")
T.printTree(T.root)
print("After:")
T2 = BST()
T2.dupwayfix(T.root)
T2.printTree(T2.root)