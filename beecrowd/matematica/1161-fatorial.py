def fatorial(number):
    if number == 0:
        return 1
    return number * fatorial(number - 1)

def main():
    while True:
        try:
            n1, n2 = input().split()
            result = fatorial(int(n1)) + fatorial(int(n2))
            print(result)
        except EOFError:
            break

if __name__ == '__main__':
    main()