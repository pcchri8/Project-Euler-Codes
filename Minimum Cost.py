from itertools import combinations


def solve(N, M, Arr):
    subsequences = list(combinations(Arr, M))  # Generate all subsequences
    min_time = Arr[0] * Arr[M - 1]  # Initialize with first subsequence’s transfer time

    for subseq in subsequences:
        transfer_time = subseq[0] * subseq[-1]
        min_time = min(min_time, transfer_time)

    return min_time

