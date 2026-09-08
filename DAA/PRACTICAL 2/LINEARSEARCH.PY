def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arr = [10, 20, 30, 40, 50]
target = 30

result = linear_search(arr, target)

print("Index:", result)

print("Best Case Time Complexity: O(1)")
print("Average Case Time Complexity: O(n)")
print("Worst Case Time Complexity: O(n)")
print("Space Complexity: O(1)")
