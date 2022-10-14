from tree_node_class import Node

class BSTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self,key):
        if self.root == None:
            self.root = Node(key)
        else:
            temp = self.root
            par = temp
            while (temp):
                par = temp
                if temp.key > key:
                    temp = temp.left
                else:
                    temp = temp.right
            if par.key > key:
                par.left = Node(key, par)

            else:
                par.right = Node(key, par) 
    
    def traverse_in2(self,node):
        if node:
            self.traverse_in2(node.left)
            print(node.key, end=", ")
            self.traverse_in2(node.right)

    def traverse_pre2(self, node):
        if node:
            print(node.key, end=", ")
            self.traverse_pre2(node.left)
            self.traverse_pre2(node.right)
    
    def traverse_post2(self, node):
        if node:
            self.traverse_post2(node.left)
            self.traverse_post2(node.right)
            print(node.key, end=", ")
    
    def traverse_bfs_iterative(self, node):
        queue = [node]
        front = rear = 0
        while(front <= rear):
            current_node = queue[front]
            front += 1
            print(current_node.key, end=", ")
            if current_node.left:
                rear += 1
                queue.append(current_node.left)
            if current_node.right:
                rear +=1
                queue.append(current_node.right)

    def bfs_recursive(self, queue):
        if len(queue):
            node = queue.pop(0)
            print(node.key, end=", ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            self.bfs_recursive(queue)

    def traverse_bfs_recursive(self, node):
        queue = [node]
        self.bfs_recursive(queue)
    
    def traverse_dfs_iterative(self, node):
        stack = [node]
        while stack:
            current_node = stack.pop()
            print(current_node.key, end=", ")
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)

    def dfs_recursive(self, stack):
        if len(stack):
            node = stack.pop()
            print(node.key, end=", ")
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            self.dfs_recursive(stack)

    def traverse_dfs_recursive(self,node):
        stack = [node]
        self.dfs_recursive(stack)

    def inorder_successor(self, node) -> Node:
        node_t = node.right
        if node_t == None:
            return None
        while(node_t.left != None):
            node_t = node_t.left
        return node_t

    # def inorder_successor_d(self, node) -> Node:
    #     node_t = node.right
    #     if node_t == None:
    #         return None
    #     if node_t.left == None:
    #         node.right = node_t.right
    #         # return node_t
    #     else:
    #         par = node
    #         while(node_t.left != None):
    #             par = node_t
    #             node_t = node_t.left
    #         par.left = None
    #     return node_t


    def delete_node(self, node):

        if node.left == None and node.right == None:    # No child 
            if node == self.root:
                self.root = Node(-1)
            else:
                if node.par.left == node:
                    node.par.left = node.left
                else:
                    node.par.right = node.right
            # return

        elif node.right != None:                          # right child - may/maynot left
            successor = self.inorder_successor(node)
            node.key = successor.key
            if successor.par.left == successor:
                successor.par.left = successor.right
            else:
                successor.par.right = successor.right           
            # return
        
        # elif node.left != None: # and node.right == None:     #only left child - no right child 
        else:                                                   # if (node.left != None) and (node.right == None)
            node.key = node.left.key
            node.right = node.left.right
            node.left = node.left.left
            # return

            

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

    def find_node(self, k):
        # implementing bfs with k nodes bound
        if self.root == None:
            return None
        queue = [self.root]
        front = rear = 0
        while(k and front <= rear):
            current_node = queue[front]
            front += 1
            k -= 1
            if current_node.left:
                rear += 1
                queue.append(current_node.left)
            if current_node.right:
                rear +=1
                queue.append(current_node.right)
        if k == 0:
            return current_node

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
    

    def diameter(self,node):
        if node == None:
            return (0,0)
        else:
            ld, lh = self.diameter(node.left) 
            rd, rh = self.diameter(node.right)
            d = lh + rh + 1
            h = max(lh, rh) + 1
            # print("key", node.key,'ld',ld, 'lh', lh, 'rd', rd, 'rh', rh, 'd', d, 'h', h)
            return (max(ld,rd,d),h)
