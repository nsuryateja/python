def sort_ascend(list_of_non_duplicates):
  """Implementing the sorting algorithm for non duplicates in a list - Ascending Order"""
  iter = 0
  while iter < len(list_of_non_duplicates):
      index_of_min = list_of_non_duplicates.index(min(list_of_non_duplicates[iter:]))
      popped_item = list_of_non_duplicates.pop(index_of_min)
      list_of_non_duplicates.insert(iter,popped_item)
      iter = iter + 1
  return list_of_non_duplicates

def sort_descend(list_of_non_duplicates):
  """Implementing the sorting algorithm for non duplicates in a list - Descending Order"""
  iter = 0
  while iter < len(list_of_non_duplicates):
      index_of_min = list_of_non_duplicates.index(min(list_of_non_duplicates[iter:]))
      popped_item = list_of_non_duplicates.pop(index_of_min)
      list_of_non_duplicates.insert(0,popped_item)
      iter = iter + 1
  return list_of_non_duplicates

print(sort_ascend([1,4,3,7,5,6]))
print(sort_descend([1,4,3,7,5,6]))


  

