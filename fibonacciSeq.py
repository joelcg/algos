def getFibNum(pos):
  if pos == 0 or pos == 1: return pos
  return getFibNum(pos - 1) + getFibNum(pos - 2)

def getFibSeq(num):
  for num in range(num):
    print(getFibNum(num))
