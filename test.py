def check_primes(n):
    if n <= 1:
        return []
    nums = [True] * (n + 1)
    nums[0], nums[1] = False, False
    for i in range(2, int(n ** 0.5) + 1):
        if nums[i]:
            for j in range(i * i, n + 1, i):
                nums[j] = False
    prime_final = []
    for i in range(2, n + 1):
        if nums[i]:
            prime_final.append(i)
    return prime_final

N = 37
print(check_primes(N))