import random


class Node:
    def __init__(self, key) -> None:
        self.key = key

def define_root(key):
    tree[0] = Node(key)

def set_left(key,parent) -> None:
    if tree[parent] == None:
        print(key, "parent is none !!")
        return
    tree[parent * 2 + 1] = Node(key)

def set_right(key, parent):
    if tree[parent] == None:
        print(key,"parent is none !!")
        return
    tree[parent * 2 + 2] = Node(key)

def print_tree():
    for i in range(n):
        if tree[i] == None:
            print(" - ", end = " ")
        else:
            print(f' %s '%tree[i].key, end = " ")

# n = random.randint(9,10)
n =10
tree = [None]*n
define_root('A')
set_right('C', 0)
set_left('D', 1)
set_right('E', 1)
set_right('F', 2)

print_tree()