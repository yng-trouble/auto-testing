from capitalize import capitalize


if capitalize 'hexlet' != 'Hexlet':
    raise Exception("Функция работает неверно!")

if capitalize("") != "":
    raise Exception("Функция работает неверно!")