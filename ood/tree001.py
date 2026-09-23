class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printTreeVisual(root, indent="", last='updown'):
    if root != None:
        print(indent, end='')
        if last == 'updown': 
            print("Root----", end='')
            indent += "       "
        elif last == 'right': 
            print("R----", end='')
            indent += "       "
        elif last == 'left': 
            print("L----", end='')
            indent += "       "
        print(root.val)
        printTreeVisual(root.left, indent, 'left')
        printTreeVisual(root.right, indent, 'right')

def build_tree(level_order_list):
    """สร้าง Binary Tree จากรายการข้อมูลแบบ Level-Order"""
    if not level_order_list:
        return None
    
    root = TreeNode(int(level_order_list[0]))
    queue = [root]
    i = 1
    
    while queue and i < len(level_order_list):
        curr = queue.pop(0)
        
        # ลูกซ้าย
        if i < len(level_order_list) and level_order_list[i] != 'null':
            curr.left = TreeNode(int(level_order_list[i]))
            queue.append(curr.left)
        i += 1
        
        # ลูกขวา
        if i < len(level_order_list) and level_order_list[i] != 'null':
            curr.right = TreeNode(int(level_order_list[i]))
            queue.append(curr.right)
        i += 1
        
    return root

def get_level_order(root):
    """ดึงข้อมูลค่าในโหนดออกมาเป็น List แบบ Level-Order"""
    if not root:
        return []
    
    res = []
    queue = [root]
    while queue:
        curr = queue.pop(0)
        res.append(curr.val)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return res

def mirror_from_depth(node, target_depth, current_depth=0):
    """สลับโหนดซ้าย-ขวาเฉพาะโหนดที่อยู่ในระดับตั้งแต่ target_depth เป็นต้นไป"""
    if not node:
        return
    
    # สลับกิ่งซ้าย-ขวาของโหนดพ่อแม่ เมื่อความลึกของโหนดลูกตรงตามเงื่อนไข (>= target_depth)
    if current_depth >= target_depth - 1:
        node.left, node.right = node.right, node.left
        
    mirror_from_depth(node.left, target_depth, current_depth + 1)
    mirror_from_depth(node.right, target_depth, current_depth + 1)

# --- ส่วนประมวลผลหลัก ---
print(" *** Mirror Tree ***")
user_input = input("Enter nodes in level-order,depth : ").split(',')
nodes_str = user_input[0].split()
target_depth = int(user_input[1])

# 1. สร้างต้นไม้จาก Level-Order
root = build_tree(nodes_str)

# 2. แสดงผลก่อน Mirror
print(f"before mirror: {get_level_order(root)}")
printTreeVisual(root)

# 3. ทำการ Mirror ตั้งแต่ระดับ Depth ที่กำหนด
mirror_from_depth(root, target_depth)

# 4. แสดงผลหลัง Mirror
print(f"after mirror : {get_level_order(root)}")
printTreeVisual(root)