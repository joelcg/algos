class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sum(root):
  if root == None: return 0
  return root.data + sum(root.left) + sum(root.right)
