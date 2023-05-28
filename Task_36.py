def capitalize(string1, string2):
    res = []

    for i in string1:
        res.append(i.upper())
        break

    for k in string2:
        res.append(k.upper())
        break

    return res


print(capitalize("Никита", "Петросян"))
