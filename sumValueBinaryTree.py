class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sumValue(root):
  if root == 0; return None
  return root.data + sumValue(root.left) + sumValue(root.right)
