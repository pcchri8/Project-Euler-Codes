def Solve(N):
    if N == 1:
        return "NO"

    if N < 1 or N > 10**9:
        print("NO")
        return 0

    if N == 0:
        print("NO")
        return 0

    sum_divisors = 1
    iteration_max = int(N ** 0.5)

    for i in range(2, iteration_max + 1):
        if N % i == 0:
            sum_divisors += i
            if i != N // i:
                sum_divisors += N // i

    return "YES" if sum_divisors == N else "NO"


T = int(input())
if T < 1 or T > 100:
    Solve(0)
else:
    for _ in range(T):
        N = int(input())
        out_ = Solve(N)
        print(out_)
