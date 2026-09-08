def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Main program
n = 5

print("Number:", n)
print("Factorial:", factorial(n))

# Time Complexity
print("Time Complexity: O(n)")

# Space Complexity
print("Space Complexity: O(n)")
