def fibonacci(n, k):
    fib = [1, 1]
    if n <= 1:
        return 1
    else:
        n -= 1
        for _ in range(n):
            amount = (fib[0] + fib[1]) % (10 ** k)
            fib[0], fib[1] = fib[1], amount
            result = fib[1]
    return result


if __name__ == '__main__':
    n, k = list(map(int, (input()).split()))
    print(fibonacci(n, k))
