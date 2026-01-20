N = 100000

def get_proper_divisors_sum(n):

    if n <= 1:
        return 0
    divisors = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sum(divisors)

def generate_divisors_sum_dict(limit):

    return {n: get_proper_divisors_sum(n) for n in range(1, limit + 1)}

def get_amicable_numbers(limit):
    divisors_sum_dict = generate_divisors_sum_dict(limit)
    return {n for n in range(1, limit + 1) if divisors_sum_dict.get(n) != n and divisors_sum_dict.get(divisors_sum_dict.get(n)) == n}

print(f"The sum of all amicable numbers up to {N} is {sum(get_amicable_numbers(N))}")

