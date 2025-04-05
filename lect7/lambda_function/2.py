# Sample input
numbers = [10, 6, 8, 90, 12, 56]

# Lambda function to find max and min
max_min_tuple = lambda lst: (max(lst), min(lst))

# Example usage:
result = max_min_tuple(numbers)
print(f"Maximum and minimum values in the list are: {result}")
