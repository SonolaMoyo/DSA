class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, data):
        if self.root.value:
            if data < self.root.value:
                if self.root.left is None:
                    self.root.left = Node(data)
                else:
                    self.root.left = Node(data)
            elif data > self.root.value:
                if self.root.right is None:
                    self.root.right = Node(data)
                else:
                    self.root.right = Node(data)
        else:
            self.root.value = data

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
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print (tree.search(4))
# Should be False
print (tree.search(6))