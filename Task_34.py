def multiplication_table(limit):
    count = 0
    for i in range(2, 10):
        for k in range(2, 10):
            print(f"{i} * {k} = {i * k}")
            count += 1
            if count == limit:
                return
            else:
                pass


multiplication_table(10)
