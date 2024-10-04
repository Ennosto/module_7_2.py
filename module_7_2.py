def custom_write(file_name: str, strings: list[str]):
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    i = 0
    for str_ in strings:
        i += 1
        strings_positions[(i, file.tell())] = f'{str_}'
        file.write(f'{str_}\n')
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
