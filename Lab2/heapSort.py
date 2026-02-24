def heap_sort(arr):
  a = arr[:]
  n = len(a)
  
  for i in range(n // 2- 1,-1,-1):
    _heapify(a, n, i)
    
  for i in range(n- 1, 0,-1):
    a[0], a[i] = a[i], a[0]
    _heapify(a, i, 0)
    
return a


def _heapify(a,heap_size,root_index):
  largest = root_index
  left = 2* root_index +1
  right= 2*root_index+ 2
  
  if left <heap_size and a[left] >a[largest]:
    largest= left
  if right <heap_size and a[right] >a[largest]:
    largest= right
  if largest != root_index:
  a[root_index], a[largest] =a[largest], a[root_index]
  _heapify(a,heap_size,largest)
