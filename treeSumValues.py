class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def sumValues(root):
  if root == None:
    return 0
  return root.data + sumValues(root.left) + sumValues(root.right)
