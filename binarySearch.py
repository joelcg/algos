def binarySearch(data, val):
  low = 0
  high = len(data)-1
  iterCount = 0
  while low <= high:
    mid = int((low + high)/2)
    iterCount += 1
    print("iterasi ke", iterCount)
    if data[mid] == val:
      return mid
    elif data[mid] < val:
      low = mid + 1
    else:
      high = mid - 1
  return "Tidak ada hasil."
