tests = int(input())


def remove_letters(value: str):
    number = ''
    for char in value:
        if char.isnumeric():
            number += char
    return int(number)


value = 0
for _ in range(tests):
    value += remove_letters(input())

print(value)
