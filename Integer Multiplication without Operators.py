def multiply(a, b):
    result = 0
    for _ in range(abs(b)):
        result += a
    if b < 0:
        result = -result
    return result

# Test the function
print(multiply(3, 4))
print(multiply(-2, 5))
