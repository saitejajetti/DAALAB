def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


# Main program
arr = [10, 20, 30, 40, 50, 60, 70]
target = 50

result = binary_search(arr, target)

print("Index:", result)

# Time Complexity
print("Best Case Time Complexity: O(1)")
print("Average Case Time Complexity: O(log n)")
print("Worst Case Time Complexity: O(log n)")

# Space Complexity
print("Space Complexity: O(1)")
