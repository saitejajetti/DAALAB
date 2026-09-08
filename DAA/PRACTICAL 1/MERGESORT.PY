def merge_sort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        # Sort left and right halves
        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        # Merge the two sorted halves
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy remaining elements from left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Copy remaining elements from right
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


# Main program
arr = [38, 27, 43, 3, 9, 82, 10]

print("Original Array:", arr)

merge_sort(arr)

print("Sorted Array:", arr)

# Time Complexity
print("Best Case Time Complexity: O(n log n)")
print("Average Case Time Complexity: O(n log n)")
print("Worst Case Time Complexity: O(n log n)")

# Space Complexity
print("Space Complexity: O(n)")
