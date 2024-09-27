class Node:
    def __repr__(self):
        return str(self.value)
    
    def __init__(self, value):
        self.value = value
        self.children = []

class Tree:
    def __init__(self, value):
        self.root = Node(value)
    
    def __repr__(self):
        print_tree(self.root)
        return ''

    def add(self, target, value):
        target_node = self.search(target)
        
        if target_node:
            target_node.children.append(Node(value))
        else:
            raise ValueError('Target not found')
    
    def search(self, target):
        stack = [self.root]

        while len(stack) > 0:
            current = stack[0]

            if current.value == target:
                return current

            stack.pop(0)
            stack += current.children

        return None
            
def print_tree(node, depth = 0, isLast = False, prefix = ''):
    if depth == 0:
        print(node.value)
    else:
        branch = '└──' if isLast else '├──'
        print(f'{prefix}{branch} {node.value}')
    
    new_prefix = prefix
    if depth > 0:
        new_prefix += '    ' if isLast else '│   '

    for i, child in enumerate(node.children):
        isLastChild = (i == len(node.children) - 1)
        print_tree(child, depth + 1, isLastChild, new_prefix)

tree = Tree(1)

tree.add(1, 2)
tree.add(1, 3)

tree.add(2, 20)
tree.add(2, 21)

tree.add(20, 200)
tree.add(20, 201)

tree.add(21, 210)
tree.add(21, 211)

tree.add(3, 30)
tree.add(3, 31)

tree.add(30, 300)
tree.add(30, 301)

tree.add(31, 310)
tree.add(31, 311)

print(tree)

