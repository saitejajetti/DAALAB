def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = []
    right = []

    for x in arr[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    return quick_sort(left) + [pivot] + quick_sort(right)


# Main program
arr = [10, 7, 8, 9, 1, 5]

print("Original Array:", arr)

arr = quick_sort(arr)

print("Sorted Array:", arr)

# Time Complexity
print("Best Case Time Complexity: O(n log n)")
print("Average Case Time Complexity: O(n log n)")
print("Worst Case Time Complexity: O(n^2)")

# Space Complexity
print("Space Complexity: O(n)")
