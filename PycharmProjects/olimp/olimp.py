N = int(input())
K = int(input())
if 1 <= N <= 10 ** 4:
    if (1 <= K <= N) and ((N % K) == 0):
        print(2 * N * (N // K - 1))
