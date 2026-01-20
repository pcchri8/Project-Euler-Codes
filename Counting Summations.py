def partitions(n):
    """
    Return the number of integer partitions of n using the pentagonal number theorem recurrence.
    """
    p = [0] * (n + 1)
    p[0] = 1

    for i in range(1, n + 1):
        k = 1
        while True:
            pent1 = k * (3 * k - 1) // 2
            if pent1 > i:
                break
            sign = 1 if k % 2 else -1
            p[i] += sign * p[i - pent1]

            pent2 = k * (3 * k + 1) // 2
            if pent2 > i:
                k += 1
                continue
            p[i] += sign * p[i - pent2]
            k += 1

    return p[n]


def main():
    n = 100
    total_partitions = partitions(n)
    # Subtract the single-part partition (n itself)
    result = total_partitions - 1
    print(result)


if __name__ == "__main__":
    main()