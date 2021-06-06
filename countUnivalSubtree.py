class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def unival(root):
  if root == None: return 0
  if root.left == None and root.right == None: return 1
  if root.left.data == root.right.data == root.data:
    return unival(root.left) + unival(root.right) + 1
  return unival(root.left) + unival(root.right)
