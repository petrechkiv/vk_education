# считываем строку со стандартного ввода
input_string = input()

# приводим строку к нижнему регистру

lowercased_string = input_string.lower()

# заменяем символы "!","%", "#", "@" на пустую строку

replaced_string = lowercased_string.replace("!", "").replace("%", "").replace("#", "").replace("@", "")

# считаем количество замененных символов

replaced_chars_count = len(lowercased_string) - len(replaced_string)

# выводим результат

print(replaced_chars_count)

print(replaced_string)
