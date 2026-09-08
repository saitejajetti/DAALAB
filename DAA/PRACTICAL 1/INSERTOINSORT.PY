def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


# Main program
arr = [12, 11, 13, 5, 6]

print("Original Array:", arr)

insertion_sort(arr)

print("Sorted Array:", arr)

# Time Complexity
print("Best Case Time Complexity: O(n)")
print("Average Case Time Complexity: O(n^2)")
print("Worst Case Time Complexity: O(n^2)")

# Space Complexity
print("Space Complexity: O(1)")
