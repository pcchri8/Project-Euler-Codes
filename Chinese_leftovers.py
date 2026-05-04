import math

LO = 1_000_000
HI = 1_005_000

# Compute phi values up to HI - 1
phi = list(range(HI))

for i in range(2, HI):
    if phi[i] == i:  # prime
        for j in range(i, HI, i):
            phi[j] -= phi[j] // i


def crt_smallest(a, n, b, m):
    d = math.gcd(n, m)

    if (b - a) % d != 0:
        return 0

    n1 = n // d
    m1 = m // d

    # Solve:
    # n1 * t = (b-a)/d mod m1
    t = ((b - a) // d * pow(n1, -1, m1)) % m1

    lcm = n * m1
    return (a + n * t) % lcm


ans = 0

for n in range(LO, HI):
    for m in range(n + 1, HI):
        ans += crt_smallest(phi[n], n, phi[m], m)

print(ans)