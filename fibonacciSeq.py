def getFibNumRec(pos):
  if pos == 0 or pos == 1: return pos
  return getFibNumRec(pos - 1) + getFibNumRec(pos - 2)

def getFibSeqRec(num):
  for num in range(num):
    print(getFibNumRec(num))
