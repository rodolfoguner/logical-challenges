from typing import List


def main() -> None:
    
    i: int = 1
    
    while True:
        participants_quantity: int = int(input())
        
        if participants_quantity <= 0 or participants_quantity > 10_000:
            break

        participants: List[int] = [int(num) for num in input().split()]
        winner: int = 0
        
        if participants_quantity != len(participants):
            break
        
        for j, participant in enumerate(participants, start=1):
            if j == participant:
                winner = participant
                break

        print(f'Teste {i}')
        print(winner)
        print()
        i += 1


if __name__ == '__main__':
    main()
