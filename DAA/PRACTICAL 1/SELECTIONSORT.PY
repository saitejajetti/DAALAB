def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap minimum element with current element
        arr[i], arr[min_index] = arr[min_index], arr[i]


# Main program
arr = [64, 25, 12, 22, 11]

print("Original Array:", arr)

selection_sort(arr)

print("Sorted Array:", arr)

# Time Complexity
print("Best Case Time Complexity: O(n^2)")
print("Average Case Time Complexity: O(n^2)")
print("Worst Case Time Complexity: O(n^2)")

# Space Complexity
print("Space Complexity: O(1)")
