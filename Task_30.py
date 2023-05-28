def letter_count(string):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    vow_count = 0
    con_count = 0
    res = []
    for i in string:
        if i in vowels:
            vow_count += 1
        else:
            con_count += 1


    res.append(vow_count)
    res.append(con_count)
    return res


letter_count1 = letter_count("СтрокА")
print(f"Гласных букв {letter_count1[0]}, согласных букв {letter_count1[1]}")
