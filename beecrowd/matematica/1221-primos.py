import math

def check_prime_numbers(number):
    if number % 2 == 0 and number > 2:
        return False
    return all(number % i for i in range(3, int(math.sqrt(number)) +1, 2))

def main():
    inputs = int(input())
    for _ in range(inputs):
        number = int(input())
        if check_prime_numbers(number):
            print('Prime')
        else:
            print('Not Prime')

if __name__ == '__main__':
    main()