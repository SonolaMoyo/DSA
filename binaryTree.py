class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        values = self.print_tree(self.root)
        if find_val in values:
            return True
        else:
            return False

    def print_tree(self, root):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        res = []
        if root:
            res.append(root.value)
            res = res + self.print_tree(root.left)
            res = res + self.print_tree(root.right)
        return res
        

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        # if self.left:
        #     self.left.PrintTree()
        # print( self.data),
        # if self.right:
        #     self.right.PrintTree()
        return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print (tree.search(4))
# Should be False
print (tree.search(6))

# Test print_tree
# Should be 1-2-4-5-3
res = tree.print_tree(tree.root)
report = ""
for r in res:
    report += f"{r}-"
    
print(report[:-1])