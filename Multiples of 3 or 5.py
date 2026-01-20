arr = []
n = 1000
for i in range(n):
    arr.append(n-i)

m3 = [ num % 3 for num in arr]
m5 = [ num % 5 for num in arr]
m = [a * b for a, b in zip(m3, m5)]

Multiples_of_3_or_5 = [num for num, mod in zip(arr, m) if mod == 0]
print(Multiples_of_3_or_5)
result = sum(Multiples_of_3_or_5)
print(result)