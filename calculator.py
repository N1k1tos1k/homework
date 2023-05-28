

def addition(arg1, arg2):
    check_number = True
    try:
        arg1 = int(arg1)
        arg2 = int(arg2)
    except ValueError:
        check_number = False


    if check_number:
        res = arg1 + arg2
    else:
        res = "Некорректный тип аргументов"
    return res



def subtraction(arg1, arg2):
    check_number = True
    try:
        arg1 = int(arg1)
        arg2 = int(arg2)
    except ValueError:
        check_number = False
    if check_number:
        res = arg1 - arg2
    else:
        res = "Некорректный тип аргументов"
    return res



def multiplication(arg1, arg2):
    check_number = True
    try:
        arg1 = int(arg1)
        arg2 = int(arg2)
    except ValueError:
        check_number = False
    if check_number:
        res = arg1 * arg2
    else:
        res = "Некорректный тип аргументов"
    return res



def division(arg1, arg2):
    check_number = True
    try:
        arg1 = int(arg1)
        arg2 = int(arg2)
    except ValueError:
        check_number = False
    if check_number:
        if arg2 == 0:
            res = "Деление на 0!"
        else:
            res = arg1 / arg2
    else:
        res = "Некорректный тип аргументов"
    return res
