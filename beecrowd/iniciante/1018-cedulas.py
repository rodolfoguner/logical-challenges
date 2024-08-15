def get_cedules(value):
    cedules = [100, 50, 20, 10, 5, 2, 1]
    returned_cedules = {
        100: 0,
        50: 0,
        20: 0,
        10: 0,
        5: 0,
        2: 0,
        1: 0,
    }
    for cedule in cedules:
        while True:
            if value - cedule >= 0:
                value -= cedule
                returned_cedules[cedule] = returned_cedules[cedule] + 1
            else:
                break
    return returned_cedules

def main():
    value = int(input())
    cedules = get_cedules(value)
    print(value)
    for key, val in cedules.items():
        print(f'{val} nota(s) de R$ {key},00')


if __name__ == '__main__':
    main()