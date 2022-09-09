"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
# function to find the partition position
def partition(array, low, high):

  # choose the rightmost element as pivot
  pivot = array[high]

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i + 1

def quicksort(array, low, high):
    if low < high:

        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # recursive call on the left of pivot
        quicksort(array, low, pi - 1)

        # recursive call on the right of pivot
        quicksort(array, pi + 1, high)

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
# print (quicksort(test, 0, len(test) - 1))
quicksort(test, 0, len(test) - 1)
print(test)