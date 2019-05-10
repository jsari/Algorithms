
#
# Definition:
# The Euler's totient function counts the positive integers up to a given integer n
# that are relatively prime to n.
#
# The following algorithm uses Euler's product formula.


def phi(n):

    ans = n
    cnt = 0
    while n % 2 == 0:
        n //= 2
        cnt += 1

    if cnt > 0:
        ans = ans // 2

    i = 3
    while i * i <= n:
        cnt = 0
        while n % i == 0:
            n //= i
            cnt += 1

        if cnt > 0:
            ans = (ans * (i - 1)) // i
        i += 2

    if n > 1:
        ans = ans * (n - 1) // n

    return ans


if __name__ == "__main__":
    for i in range(1, 100):
        print(phi(i))
