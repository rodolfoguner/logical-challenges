winners = ['A', 'B', 'C']
while True:
    try:
        values = list(map(int, input().split()))
        n_zeros = 0
        for value in values:
            if value == 0:
                n_zeros += 1
        
        if n_zeros == 0 or n_zeros == 3:
            print('*')
        elif n_zeros == 1:
            print(winners[values.index(0)])
        else:
            print(winners[values.index(1)])
        
    except EOFError:
        break