from binary_search_tree_class import BSTree
import random
from tree_node_class import Node

# =========== Check the Node class only=============== 
def check_node_class():
    root = Node(4)
    root.insert_left(2)
    root.insert_right(6)
    root.left.insert_left(1)
    root.left.insert_right(3)
    root.right.insert_left(5)
    root.right.insert_right(7)

    root.traverse_in()
    root.traverse_in2(root)


# ========== Check the BST class ====================
def create_bst(n,lst = None) -> BSTree:
    tree = BSTree()
    # lst = [3,5,4,2,6,1,7,8,0,9]
    if lst == None:
        lst = [random.randint(0,50) for _ in range(n)]
    print(lst)
    for i in lst:
        tree.insert(i)
    return tree

# ======= Check all the traversals =================
def runTraversal(tree,*arr):
    if 'in' in arr:
        tree.traverse_in2(tree.root)
        print("IN-ORDER")
    if 'pre' in arr:
        tree.traverse_pre2(tree.root)
        print("PRE-ORDER")
    if 'post' in arr:
        tree.traverse_post2(tree.root)
        print("POST-ORDER")
    if 'bsf-i' in arr or 'bfs' in arr:
        tree.traverse_bfs_iterative(tree.root)
        print("BFS-'left to right (Iterative)'")
    if 'bfs-r' in arr:
        tree.traverse_bfs_recursive(tree.root)
        print("BFS-'left to right (recursive)'")
    if 'dfs-i' in arr or 'dfs' in arr:
        tree.traverse_dfs_iterative(tree.root)
        print("DFS-'left to right (iterative)'")
    if 'dfs-r' in arr:
        tree.traverse_dfs_recursive(tree.root)
        print("DFS-'left to right (recursive)'")

# ====== Check the disply function - copied from S.O.F. =====
def print_tree(tree):
    tree.display(tree.root)

# ======== check find nth node level order ==========
def find_the_node(tree, n, k=None) -> Node :
    if k ==  None:
        k = random.randint(1,n)
    tree.traverse_bfs_iterative(tree.root)
    node = tree.find_node(k)
    print('\n',k,'- number node is ',node.key)
    return node

# ===== Check the delete node function ============
# ====== delete kth node in tree =============
def delete_node(tree,node):
    tree.delete_node(node)
    # lst.sort()
    # print(lst[lst.index(tree.root.key) :])



# =========== delete root node =================


if __name__ == '__main__':
    k = 6
    n = 12
    tree = create_bst(n)
    runTraversal(tree, 'bst')
    print_tree(tree)
    node = find_the_node(tree,n)
    delete_node(tree, node)
    print_tree(tree)

