
def sieve(n):
    # Generate all prime numbers less than or equal to n
    #
    # Time complexity : O(n*log(log(n)))

    is_prime = [False, False] + [True] * (n - 1)

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return [i for i, x in enumerate(is_prime) if x]


if __name__ == "__main__":
    print(*sieve(10000))
