def collatz_memorized(limit):
    # Dictionary to store the chain lengths for computed numbers
    chain_lengths = {}

    def collatz_chain_length(num):
        if num in chain_lengths:
            return chain_lengths[num]

        if num == 1:
            return 1

        if num % 2 == 0:
            next_num = num // 2
        else:
            next_num = 3 * num + 1

        # Recursively calculate and store the result
        length = 1 + collatz_chain_length(next_num)
        chain_lengths[num] = length
        return length

    # Compute the chain lengths for all numbers from 1 to limit
    for n in range(1, limit + 1):
        collatz_chain_length(n)

    return chain_lengths


result_dict = collatz_memorized(999999)

longest_chain_number = max(result_dict, key=result_dict.get)
longest_chain_length = result_dict[longest_chain_number]

print(f"Starting number: {longest_chain_number}, Chain length: {longest_chain_length}")
