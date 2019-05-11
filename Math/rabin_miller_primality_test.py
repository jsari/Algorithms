
def rabin_miller(n):

    # Returns True if n is prime, False otherwise
    # The algorithm is deterministic if n < 2^64

    if n < 4:
        return n in [2, 3]

    # write n as 2^r*d + 1 with d odd
    r = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    # find bases to test
    if n < 1373653:
        bases = [2, 3]
    elif n < 4759123141:
        bases = [2, 7, 61]
    elif n < 2152302898747:
        bases = [2, 3, 5, 7, 11]
    else:
        bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    for a in bases:

        if n == a:
            return True

        x = pow(a, d, n)

        if x == 1 or x == n-1:
            continue

        for _ in range(r-1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True


if __name__ == "__main__":
    print(rabin_miller(102499))
