
def check_parentheses(expression: str) -> bool:
    left_parentheses = 0
    right_parentheses = 0
    for character in expression:
        if character == ')':
            if right_parentheses >= left_parentheses:
                return False
            right_parentheses += 1
        if character == '(':
            left_parentheses += 1
            
    return left_parentheses == right_parentheses

def main() -> None:
    while True:
        try:
            expression = input()
            if check_parentheses(expression):
                print('correct')
            else:
                print('incorrect')
        except EOFError:
            break
        

if __name__=='__main__':
    main()
