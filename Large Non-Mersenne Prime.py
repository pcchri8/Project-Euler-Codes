def get_last_ten_digits(n):

    if n < 10000000000:
        return [d for d in str(n)]
    else:
        return [d for d in str(n)[-10:]]


def multiplication_last_ten_digits(n, m):

    last_ten_digits_n = get_last_ten_digits(n)
    n = int("".join(map(str, last_ten_digits_n)))
    last_ten_digits_m = get_last_ten_digits(m)
    m = int("".join(map(str, last_ten_digits_m)))
    p = int("".join(map(str, get_last_ten_digits(n*m))))

    return p


print("28433 x 2^7830457 + 1 is a massive non-Marsenne prime. We are gonna compute its last ten digits!")

# last ten digits of 2 to the power of i up to i=7830457
start = 1
for i in range(1,7830458):
    product = multiplication_last_ten_digits(start, 2)
    start = product

result = multiplication_last_ten_digits(28433, product) + 1
print(f"It's last ten digits are {result}")