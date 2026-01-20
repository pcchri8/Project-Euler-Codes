def is_prime(n):

    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))


def sum_consecutive_primes(start, end, primes):
    return sum(primes[start:end])


def longest_consecutive_prime_sum(limit):

    primes = [n for n in range(2, limit) if is_prime(n)]

    max_length = 0
    max_prime = 0
    num_primes = len(primes)

    # Two-pointer technique to find the longest sequence
    for start in range(num_primes):
        for end in range(start + max_length, num_primes):  # Start with at least max_length terms
            total = sum_consecutive_primes(start, end, primes)
            if total > limit:
                break
            if is_prime(total):
                max_length = end - start
                max_prime = total

    return max_prime, max_length

lim = 1000000
result, length = longest_consecutive_prime_sum(lim)
print(f"The prime {result} is a sum of {length} consecutive primes")