def search_min_val(list1):
    low_val = 0
    count = 0
    res = []

    list1.sort()
    for i in list1:
        if low_val <= i:
            low_val = i
            res.append(i)
            count += 1

            if count == 2:
                break
            else:
                pass

        else:
            pass

    return res


print(search_min_val([1, 6, 3, 8, 2, 10, 23, 4]))

