def sum_square(n):
    return int(n * (n + 1) * (2*n + 1) / 6)


def square_sum(n):
    return int(n * n * (n + 1) * (n + 1) / 4)


N = 100
print(square_sum(N) - sum_square(N))