from scan import *

if __name__ == '__main__':
    with open('expression.txt') as f:
        i = f.read()
        while True:
            token, type = get_token(i)
            print(length)
            if token is None:
                break
            print(token, type)