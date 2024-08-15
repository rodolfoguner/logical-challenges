NUMBER_OF_LEDS = {
    '0': 6,
    '1': 2,
    '2': 5,
    '3': 5,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 3,
    '8': 7,
    '9': 6,
}

def get_number_of_leds(display_number: str):
    number_of_leds = 0
    for number in display_number:
        number_of_leds += NUMBER_OF_LEDS.get(number, 0)
    
    return number_of_leds


def main():
    inputs = int(input())
    for _ in range(inputs):
        display_number = input()
        print(f'{get_number_of_leds(display_number)} leds')

if __name__=='__main__':
    main()