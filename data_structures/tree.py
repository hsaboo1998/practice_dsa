class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

def inOrderTraversal(node):
  if node is None:
    return
  inOrderTraversal(node.left)
  print(node.data, end=", ")
  inOrderTraversal(node.right)

inOrderTraversal(root)

def min_val_node(node):
    curr_node = node
    if node.left:
        curr_node = min_val_node(node.left)
    return curr_node

def delete_node(node, data):
    if not node:
        return None
    if node.data>data:
        node.left = delete_node(node.left, data)
    elif node.data<data:
        node.right = delete_node(node.right, data)
    else:
        if not node.left:
            return node.right
        elif not node.right:
            return node.left
        else:
            node.data = min_val_node(node.right).data
            node.right = delete_node(node.right, node.data)
    return node

root = delete_node(root, 15)

inOrderTraversal(root)

class AVLTreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.height = 0

def get_height(node):
    if not node:
        return 0
    return node.height

def get_balance(node):
    if not node:
        return 0
    return get_height(node.right) - get_height(node.left)

def right_rotate(node):
    y = node.left
    x = y.right
    y.right = node
    node.left = x
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    node.height = 1 + max(get_height(node.left), get_height(node.right))
    return y

def left_rotate(node):
    y = node.right
    x = y.left
    node.right = x
    y.left = node
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    node.height = 1 + max(get_height(node.left), get_height(node.right))
    return y

def insert(node,data):
    if not node:
        return AVLTreeNode(data)
    if data<node.data:
        node.left = insert(node.left, data)
    elif data>node.data:
        node.right = insert(node.right, data)
    node.height = 1 + max(get_height(node.left), get_height(node.right))
    # LL
    if get_balance(node)<-1 and get_balance(node.left)<0:
        node = right_rotate(node)
    # LR
    if get_balance(node)<-1 and get_balance(node.left)>0:
        node.left = left_rotate(node.left)
        node = right_rotate(node)
    # RR
    if get_balance(node)>1 and get_balance(node.right)>0:
        node = left_rotate(node)
    # RL
    if get_balance(node)>1 and get_balance(node.right)<0:
        node.right = right_rotate(node.right)
        node = left_rotate(node)
    return node

root = None
letters = ['C', 'B', 'E', 'A', 'D', 'H', 'G', 'F']
for letter in letters:
    root = insert(root, letter)

inOrderTraversal(root)