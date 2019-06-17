
key_word = ['=', '+', '-', '*', '/', '(', ')']
digit = '0123456789'
little_letters = [chr(i + 97) for i in range(26)]
big_letters = [chr(i + 65) for i in range(26)]
length = 0


def get_type(token):
    if token in key_word:
        return 'op'
    else:
        return 'digit'


def get_token(string):
    '''
    :param string:
    :return: token以及token type
    '''
    global length
    if length >= len(string):
        return None, 'end'
    else:
        while length < len(string):
            if string[length] in string[length] in digit or string[length] in little_letters or string[length] in big_letters:
                while string[length] in digit or string[length] in little_letters or string[length] in big_letters:
                    length += 1
                token = string[:length]
                type = get_type(token)
                return token, type

            elif string[length] in key_word:
                length += 1
                token = string[:length]
                type = get_type(token)
                return token, type







