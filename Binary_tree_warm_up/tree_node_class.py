class Node:
    def __init__(self, key, par = None):
        self.key = key
        self.left = None
        self.right = None
        self.par = par

    def insert_left(self, key):
        self.left =  Node(key,self)

    def insert_right(self, key):
        self.right = Node(key,self)

    def delete_left(self):
        self.left = None

    def delete_right(self):
        self.right = None

    def update_key(self, newKey):
        self.key = newKey
    
    # In this traversal method self is continuously changing wrt the node.
    def traverse_in(self):
        if self.left != None:
            self.left.traverse_in()
        print(self.key)
        if self.right != None:
            self.right.traverse_in()
    
    # In this, self is always the root node and key if fetched from `node` variable
    def traverse_in2(self,node):
        if node:
            self.traverse_in2(node.left)
            print(node.key)
            self.traverse_in2(node.right)

    

