# Даны некоторые неструктурированные текстовые данные, и требуется выполнить
# их элементарную очистку.

# Большинство элементарных операций очистки текста соответствуют элементарным
# операциям языка Python над строковыми значениями, в частности strip, replace
# и split:

# Создать текст
text_data = ["   Interrobang. By Aishwarys Henriette    ",
             "Parking And Going. By Karl Gautier",
             '     Today Is The night. By Jarek Prakash   ']

# Удалить пробелы
strip_whitespace = [string.strip() for string in text_data]
print(strip_whitespace)

# Удалить точки
remove_periods = [string.replace(".", "") for string in strip_whitespace]
print(remove_periods)


# Кроме того, мы обычно создаем и применяем собственную функцию преобразования:
def capitalizer(string: str) -> str:
    return string.upper()


print([capitalizer(string) for string in remove_periods])

# Наконец, для выполнения мощных строковых операций можно воспользоваться
# регулярными выражениями
import re


def replace_letters_with_X(string: str) -> str:
    return re.sub(r"[a-zA-Z]", "X", string)


print([replace_letters_with_X(string) for string in remove_periods])
