def fibonacci_series(limit):
    res = [0, 1]

    for i in range(2, limit):
        res.append(res[i - 2] + res[i - 1])
    return res


print(fibonacci_series(20))
