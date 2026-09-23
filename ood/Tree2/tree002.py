str001 = list(map(int, input("Enter Input : ").split()))

class node:
	def __init__(self,value):
		self.val = value
		self.parent = None
		self.right = None
		self.left = None

	def printnode(self,node,level = 0):
		if (node == None):
			return
		self.printnode(node.right,level + 1)
		print('     ' * level, node.val)
		self.printnode(node.left,level + 1)

class tree:
	def __init__(self):
		self.root = None

	def addnode(self, val):
			if self.root == None:
				self.root = node(val)
			else:
				nownode = self.root
				while nownode != None:
					if val >= nownode.val and nownode.right != None:
						nownode = nownode.right
					elif val < nownode.val and nownode.left != None:
						nownode = nownode.left
					else:
						break
						
				newnode = node(val)
				if val >= nownode.val:
					nownode.right = newnode
					newnode.parent = nownode
				else:
					nownode.left = newnode
					newnode.parent = nownode

				check_node = newnode.parent
				while check_node != None:
					bf = self.get_balance(check_node)

					if bf > 1:
						if val < check_node.left.val:
							self.right_rotate(check_node)
						else:                        
							self.left_rotate(check_node.left)
							self.right_rotate(check_node)

					elif bf < -1:
						if val >= check_node.right.val:
							self.left_rotate(check_node)
						else:                          
							self.right_rotate(check_node.right)
							self.left_rotate(check_node)

					check_node = check_node.parent 

	def right_rotate(self, y):
			x = y.left
			T2 = x.right

			x.right = y
			y.left = T2

			x.parent = y.parent
			y.parent = x
			if T2 != None:
				T2.parent = y

			if x.parent == None:
				self.root = x
			elif x.parent.left == y:
				x.parent.left = x
			else:
				x.parent.right = x

	def left_rotate(self, x):
			y = x.right
			T2 = y.left

			y.left = x
			x.right = T2

			y.parent = x.parent
			x.parent = y
			if T2 != None:
				T2.parent = x

			if y.parent == None:
				self.root = y
			elif y.parent.left == x:
				y.parent.left = y
			else:
				y.parent.right = y

	def print_tree(self):
		self.root.printnode(self.root,0)
		print("--------------------------------------------------")

	def get_height(self, node):
		if not node:
			return 0
		return 1 + max(self.get_height(node.left), self.get_height(node.right))

	def get_balance(self, node):
		if not node:
			return 0
		return self.get_height(node.left) - self.get_height(node.right)

	def balancing(self,node,type):
		if type == "LL":
			ppp = None
			pp = node.parent.parent
			p = node.parent
			if node.parent.parent != None and node.parent.parent.parent != None:
				ppp = node.parent.parent.parent
				if ppp.left == pp:
					ppp.left = p
				else:
					ppp.right = p
				p.parent = ppp
			else:
				self.root = p
			pp.parent = p
			p.right = pp
		elif type == "RR":
			ppp = None
			pp = node.parent.parent
			p = node.parent
			if node.parent.parent != None and node.parent.parent.parent != None:
				ppp = node.parent.parent.parent
				if ppp.left == pp:
					ppp.left = p
				else:
					ppp.right = p
				p.parent = ppp
			else:
				self.root = p
			pp.parent = p
			p.left = pp
		elif type == "LR":
			ppp = None
			pp = node.parent.parent
			p = node.parent
			if node.parent.parent != None and node.parent.parent.parent != None:
				ppp = node.parent.parent.parent
				if ppp.left == pp:
					ppp.left = node
				else:
					ppp.right = node
				node.parent = ppp
			else:
				self.root = node
			p.right = None
			p.parent = node
			pp.left = None
			pp.parent = node
		elif type == "RL":
			ppp = None
			pp = node.parent.parent
			p = node.parent
			if node.parent.parent != None and node.parent.parent.parent != None:
				ppp = node.parent.parent.parent
				if ppp.left == pp:
					ppp.left = node
				else:
					ppp.right = node
				node.parent = ppp
			else:
				self.root = node
			p.left = None
			p.parent = node
			pp.right = None
			pp.parent = node

def creatavlnode(list1):
	newtree = tree()
	for i in list1:
		print(f"Insert : ( {i} )")
		newtree.addnode(i)
		newtree.print_tree()

creatavlnode(str001)