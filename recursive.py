def factorial_recursive(n):
  if n < 0:
    return "Factorial is not defined for negative numbers."

  # Base case: 0! and 1! are both 1
  if n == 0 or n == 1:
    return 1

  # Recursive step
  return n * factorial_recursive(n - 1)


# Example usage:
print(factorial_recursive(5))  # Output: 120