def symbol_count(string):
    res = {}
    for i in string:
        count = 0
        for k in string:
            if i == k:
                count += 1
            else:
                pass
        res[i] = count
    return res


print(symbol_count("Никита"))
