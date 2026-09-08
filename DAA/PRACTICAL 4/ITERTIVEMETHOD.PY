def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result


# Main program
n = 5

print("Number:", n)
print("Factorial:", factorial(n))

# Time Complexity
print("Time Complexity: O(n)")

# Space Complexity
print("Space Complexity: O(1)")
