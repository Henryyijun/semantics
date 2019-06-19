from syntax_tree import *
key_word = ['=', '+', '-', '*', '/', '(', ')']
digit = '0123456789'
little_letters = [chr(i + 97) for i in range(26)]
big_letters = [chr(i + 65) for i in range(26)]
length = 0

'''
S->id = E1
E-> E1 + E| E1 * E | E1-E | E1 /E | (E) | -E
E->id
E1->id
E2->id
E1->id

'''


class Quadruple:
    '''
    四元式数据结构
    '''
    def __init__(self, op, arg1, arg2, result):
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2
        self.result = result

    def __str__(self):
        return '(' + self.op + ',' + self.arg1 + ',' + self.arg2 + ',' + self.result + ')'


def get_type(token):
    if token in key_word:
        return 'op'
    else:
        return 'id'


def get_token(string):
    '''
    :param string:
    :return: token以及token type
    '''
    global length
    if length >= len(string):
        return None, None
    else:
        while length < len(string):
            start = length
            if string[length] in digit or string[length] in little_letters or string[length] in big_letters:
                length += 1
                token = string[start:length]
                type = get_type(token)
                return token, type

            elif string[length] in key_word:
                length += 1
                token = string[start:length]
                type = get_type(token)
                return token, type


temp = [0 for i in range(100)] #临时变量编号
quadruples = [] #四元式列表
sysmbol = {1:2, 2:1} #符号表


def gen(op, arg1, arg2, result):
    q = Quadruple(op, sysmbol[arg1], sysmbol[arg2], sysmbol[result])
    quadruples.append(q)
    return len(quadruples)


def new_temp():
    for i in range(100):
        if temp[i] == 0:
            temp[i] = -(i + 1) # < 0 表示临时变量
            return temp[i]


def lookup(name):
    '''
    以Name查符号表，若查到则返回相应登记项的序号(≥1),否则返回0。
    :param name:
    :return:
    '''
    for i, e in enumerate(sysmbol):
        if e == name:
            return i if i >= 1 else 0


def enter(name):
    keys = list(sysmbol.keys())
    keys = keys.sort()
    num = keys[len(keys) - 1]
    sysmbol.update({num:name})
    return num


def entry(name):
    i  = lookup(name)
    if i != 0:
        return i
    else:
        return enter(name)



tree = Node('S')
token = ''
type = ''

def S(i):
    token, type = get_token(i)
    print(token, type)
    if type == 'id':
        tree.children.append(Node(token))
        token, type = get_token(i)

        if token == '=' and type == 'op':
            print(token, type)
            tree.children.append(Node(token))
            #token, type = get_token(i)
            tree.children.append(E(i))


def E(i):
    global token, type

    node = Node('E')
    node.children.append(E1(i))
    print(token, type)
    if token == '+':
        node.children.append(Node(token))
        n = E(i)
        if n is not None:
            node.children.append(n)
        else:
            return None
        token, type = get_token(i)
    elif token == '-':
        node.children.append(Node(token))
        n = E(i)
        if n is not None:
            node.children.append(n)
        else:
            return None
        token, type = get_token(i)
    elif token == '/':
        node.children.append(Node(token))
        n = E(i)
        if n is not None:
            node.children.append(n)
        else:
            return None
        token, type = get_token(i)
    elif type == 'id':
        node.children.append(Node(token))
        n = E(i)
        if n is not None:
            node.children.append(n)
        else:
            return None
        token, type = get_token(i)
    return node


def E1(i):
    token, type = get_token(i)
    print(token, type)
    if type == 'id':
        token, type = get_token(i)
        print(token, type)
        return Node(token)


def parse():
    with open('expression.txt') as f:
        line = f.read()
        lines = line.split(';')
        for i in lines:
            i = i.strip(' ')
            length = 0
            S(i)


if __name__ == '__main__':
    parse()
    t = Tree()
    t.print_tree(tree)


