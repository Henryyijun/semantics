class Node:
    def __init__(self, v, place=None):
        self.value = v
        self.children = []
        self.place = place

    def __str__(self):
        return self.value + ' ' + self.node_kind + ' '


class Tree:
    def __init__(self):
        pass

    def check(self, left, nodes):
        for i in range(len(nodes)):
            if left == nodes[i].value:
                return i
        return -1


    def print_tree(self, root):
        if root is not None :
            if len(root.children) > 0:
                print(root.value, '(', end='')
                for n in root.children:
                    self.print_tree(n)
                print(')', end='')
            else:
                print(root.value, end='')
        elif root is not None:
            print(root.value, end='')