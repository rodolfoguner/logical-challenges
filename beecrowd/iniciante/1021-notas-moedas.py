def get_cedules(value):
    cedules = [10000, 5000, 2000, 1000, 500, 200]
    returned_cedules = {cedule: 0 for cedule in cedules}

    for cedule in cedules:
        while value >= cedule:
            value -= cedule
            returned_cedules[cedule] += 1

    return returned_cedules, value


def get_coins(value):
    coins = [100, 50, 25, 10, 5, 1]
    returned_coins = {coin: 0 for coin in coins}

    for coin in coins:
        while value >= coin:
            value -= coin
            returned_coins[coin] += 1

    return returned_coins


def main():
    value = float(input())
    value_in_cents = int(round(value * 100))

    cedules, value_in_cents = get_cedules(value_in_cents)
    coins = get_coins(value_in_cents)

    print('NOTAS:')
    for key, val in cedules.items():
        print(f'{val} nota(s) de R$ {key // 100:.2f}')

    print('MOEDAS:')
    for key, val in coins.items():
        print(f'{val} moeda(s) de R$ {key / 100:.2f}')


if __name__ == '__main__':
    main()
