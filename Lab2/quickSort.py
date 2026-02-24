def quick_sort(arr):
  a = arr[:]
  _quick_sort_recursive(a, 0, len(a)- 1)
  return a
  
def _quick_sort_recursive(a, low, high):
  if low < high:
    p = _partition(a, low, high)
    _quick_sort_recursive(a, low, p- 1)
    _quick_sort_recursive(a, p + 1, high)
    
def _partition(a, low, high):
  pivot = a[high]
  i = low- 1
  for j in range(low, high):
    if a[j] <= pivot:
      i += 1
      a[i], a[j] = a[j], a[i]
  a[i + 1], a[high] = a[high], a[i + 1]
  return i + 1
