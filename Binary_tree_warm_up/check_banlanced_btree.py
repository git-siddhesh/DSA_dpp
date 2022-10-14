import random


class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None
        self.par = None


class Btree:
    def __init__(self) -> None:
        self.root = None

    def bfs(self) -> None:
        queue = [self.root]
        front = rear = 0
        while ( front <= rear):
            current_node = queue[front]
            front += 1
            print(current_node.key, end=" ,")
            if current_node.left:
                queue.append(current_node.left)
                rear += 1
            if current_node.right:
                queue.append(current_node.right)
                rear += 1
        print("\n")

    def insert(self, key) -> None:
        if self.root == None:
            self.root = Node(key)
        else:
            temp = self.root
            par = temp
            while temp:
                if key < temp.key:
                    par = temp
                    temp = temp.left
                else:
                    par = temp
                    temp = temp.right
            if key < par.key:
                par.left = Node(key)
            else: 
                par.right = Node(key)
    
    
    def display(self, root):
        lines, *_ = self._display_aux(root)
        for line in lines:
            print(line)

    def _display_aux(self, root):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if root.right is None and root.left is None:
            line = '%s' % root.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if root.right is None:
            lines, n, p, x = self._display_aux(root.left)
            s = '%s' % root.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if root.left is None:
            lines, n, p, x = self._display_aux(root.right)
            s = '%s' % root.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display_aux(root.left)
        right, m, q, y = self._display_aux(root.right)
        s = '%s' % root.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


    def check_balanced(self,node):
        if node == None:
            return 0,1
        left_height, balanced = self.check_balanced(node.left)
        if balanced == -1:
            return 0,-1
        right_height, balanced = self.check_balanced(node.right)
        if balanced == -1 or abs(left_height - right_height) > 1:
            return 0 , -1
        return max(left_height, right_height) + 1, 1
    

if __name__ == '__main__':
    tree = Btree()
    n = random.randint(5,7)
    lst = [random.randint(0,20) for i in range(n) ]
    # lst = [1,2,3]
    for i in lst:
        tree.insert(i)
    
    tree.bfs()
    tree.display(tree.root)
    height, balanced = tree.check_balanced(tree.root)
    print("Balanced" if balanced == 1 else "Unbalanced")
