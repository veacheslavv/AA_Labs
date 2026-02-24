defmerge_sort(arr):
  if len(arr)<= 1:
    returnarr[:]
  mid= len(arr) //2
  left = merge_sort(arr[:mid])
  right= merge_sort(arr[mid:])
  return _merge(left,right)

def_merge(left,right):
  i= j= 0
  result = []
  while i <len(left) and j < len(right):
    if left[i]<= right[j]:
      result.append(left[i])
      i+= 1
    else:
      result.append(right[j])
      j+= 1
  result.extend(left[i:])
  result.extend(right[j:])
  returnresult
