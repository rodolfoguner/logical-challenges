cobol = ['C', 'O', 'B', 'O', 'L']
while True:
    try:
        values = input().split('-')
        result = ''
        for index, value in enumerate(values):
            if value[0].capitalize() == cobol[index] or value[-1].capitalize() == cobol[index]:
                result += cobol[index]
            else:
                break
            
        if result == 'COBOL':
            print('GRACE HOPPER')
        else:
            print('BUG')
    except EOFError:
        break