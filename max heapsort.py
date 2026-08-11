def heapify(arr, n, i):
  largest = i
  left = 2 * i + 1
  right = 2 * i + 2

  # Check if left child exists and is greater than the root
  if left < n and arr[left] > arr[largest]:
    largest = left

  # Check if right child exists and is greater than the largest so far
  if right < n and arr[right] > arr[largest]:
    largest = right

  # If the largest is not the root, swap and continue heapifying
  if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i]  # Swap
    heapify(arr, n, largest)


def heap_sort(arr):
  n = len(arr)

  # Step 1: Build a max heap
  for i in range(n // 2 - 1, -1, -1):
    heapify(arr, n, i)

  # Step 2: Extract elements from the heap one by one
  for i in range(n - 1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]  # Move current root to end
    heapify(arr, i, 0)  # Call max heapify on the reduced heap

  return arr


# Example usage:
if __name__ == "__main__":
  numbers = [12, 11, 13, 5, 6, 7]
  print("Original array:", numbers)

  sorted_numbers = heap_sort(numbers)
  print("Sorted array:", sorted_numbers)