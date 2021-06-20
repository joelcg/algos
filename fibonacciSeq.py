def getFibNumRec(pos):
  if pos == 0 or pos == 1: return pos
  return getFibNumRec(pos - 1) + getFibNumRec(pos - 2)

def getFibSeqRec(num):
  for num in range(num):
    print(getFibNumRec(num))
    
def getFibNumIte(pos):
  seq = [0,1]
  cur = 2
  while cur <= pos:
    seq.append(seq[cur-1]+seq[cur-2])
    cur += 1
  return print("Num =",str(seq[pos]),"\n","Seq =",str(seq)[1:-1])
