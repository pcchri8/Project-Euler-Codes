def count_divisors(num):
    divisors = 0
    for i in range(1, int(num**0.5) + 1): # We need only check up to sqrt of the number cause the divisors come in pairs
        if num % i == 0:
            divisors += 2 if i != num // i else 1 # Checks of the numbers are distinct divisors or it is a square root
    return divisors

def find_triangle_with_divisors(limit):
    n = 1
    triangle = 0
    while True:
        triangle += n  # Calculate the nth triangle number
        if count_divisors(triangle) > limit:
            return triangle
        n += 1

# Find the first triangle number with over 500 divisors
result = find_triangle_with_divisors(500)
print(result)
