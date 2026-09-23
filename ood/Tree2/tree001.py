str001 = str(input("Enter Input : "))
storage = []
ans = {}

def findlowest(lst):
    if not lst:
        return None
    
    lowestnode = lst[0]
    for i in lst[1:]:
        # กรณีความถี่น้อยกว่า
        if i.val < lowestnode.val:
            lowestnode = i
            
        # กรณีความถี่เท่ากัน
        elif i.val == lowestnode.val:
            # กฎ: โหนดรวม (*) ต้องถูกดึงออกมาก่อนโหนดตัวอักษร
            if i.char == '*' and lowestnode.char != '*':
                lowestnode = i
            # ถ้าเป็นตัวอักษรทั้งคู่ ให้ตัวที่ ASCII น้อยกว่ามาก่อน
            elif i.char != '*' and lowestnode.char != '*':
                if i.char < lowestnode.char:
                    lowestnode = i
                    
    lst.remove(lowestnode)
    return lowestnode

class Node:
	def __init__(self,char, value):
		self.char = char
		self.val = value
		self.right = None
		self.left = None

	def printTree(self,node,lv = 0):
		if node != None:
			self.printTree(node.right, lv + 1)
			print("     " * lv, node.char)
			self.printTree(node.left, lv + 1)

#def putpath(node,way):
#	if node == None:
#		return
#	if (node.char)[0] != "*":
#		ans[str(node.char)] = way + ans[str(node.char)]
#	putpath(node.left,way)
#	putpath(node.right,way)
def putpath(node,way):
	if (node == None):
		return 
	if ((node.char)[0] != '*'):
		ans[str(node.char)] = way
	putpath(node.right, way + "1")
	putpath(node.left, way + "0")

#def printpath(node):
#	if (node == None):
#		return 
#	if ((node.char)[0] != '*'):
#		print(f"'{str(node.char)}': '{ans[str(node.char)]}'",end = "")
#	printpath(node.right)
#	printpath(node.left)

def getans():
	while len(storage) >= 2:
		lowest1 = findlowest(storage)
		lowest2 = findlowest(storage)
		newnode = Node("*", lowest1.val + lowest2.val)
		newnode.left = lowest1
		newnode.right = lowest2
		#putpath(lowest1,"0")
		#putpath(lowest2,"1")
		storage.append(newnode)

def isinstorage(v,stro):
	for i in stro:
		if i.char == v:
			return i
	return False

for v in str001:
	node = isinstorage(v,storage)
	if node:
		node.val += 1
	else:
		newnode = Node(str(v),1)
		storage.append(newnode)

#for i in storage:
#    print(i.char, i.val)
#print("=====================")
getans()
putpath(storage[0],"")
print(ans)
storage[0].printTree(storage[0],0)
print("Encoded! : ",end="")
for i in str001:
	print(ans[i],end="")
print("")