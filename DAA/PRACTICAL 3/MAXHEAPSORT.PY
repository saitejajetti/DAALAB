def heapify(arr, n, i):
    largest = i          # Assume root is largest
    left = 2 * i + 1
    right = 2 * i + 2

    # Check left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # Heapify the affected subtree
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


# Main program
arr = [12, 11, 13, 5, 6, 7]

print("Original Array:", arr)

heap_sort(arr)

print("Sorted Array:", arr)

# Time Complexity
print("Best Case Time Complexity: O(n log n)")
print("Average Case Time Complexity: O(n log n)")
print("Worst Case Time Complexity: O(n log n)")

# Space Complexity
print("Space Complexity: O(1)")
