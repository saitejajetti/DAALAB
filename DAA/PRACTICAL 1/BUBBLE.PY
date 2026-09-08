def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        print("Pass", i + 1)

        for j in range(0, n - i - 1):
            print("Comparing", arr[j], "and", arr[j + 1])

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print("After swap:", arr)

        print("Array after pass:", arr)
        print()

    return arr


numbers = [5, 3, 8, 4, 2]

print("Original array:", numbers)

result = bubble_sort(numbers)

print("Sorted array:", result)
