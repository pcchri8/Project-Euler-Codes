from itertools import permutations
from sympy import isprime


def find_prime_permutation_sequences():
    # Generate all 4-digit prime numbers
    four_digit_primes = [n for n in range(1001, 9999, 2) if isprime(n)]

    # Group primes that are permutations of each other
    prime_permutation_groups = {}
    for prime in four_digit_primes:
        key = tuple(sorted(str(prime)))  # Unique signature for permutations
        if key in prime_permutation_groups:
            prime_permutation_groups[key].append(prime)
        else:
            prime_permutation_groups[key] = [prime]

    # Check for arithmetic sequences in these groups
    arithmetic_sequences = []
    for group in prime_permutation_groups.values():
        group.sort()  # Sort the group to check for sequences
        n = len(group)
        for i in range(n):
            for j in range(i + 1, n):
                diff = group[j] - group[i]
                third_term = group[j] + diff
                if third_term in group:
                    arithmetic_sequences.append((group[i], group[j], third_term))

    return arithmetic_sequences


if __name__ == "__main__":
    sequences = find_prime_permutation_sequences()
    for seq in sequences:
        print(f"Sequence: {seq}, Concatenated: {''.join(map(str, seq))}")