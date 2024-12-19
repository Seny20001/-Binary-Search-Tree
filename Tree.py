import turtle

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if not node.left:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        elif key > node.key:
            if not node.right:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def inorder_traversal(self):
        return self._inorder_traversal(self.root, [])

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)
        return result

    def visualize(self):
        if not self.root:
            print("Tree is empty")
            return

        screen = turtle.Screen()
        screen.title("Binary Search Tree Visualization")
        t = turtle.Turtle()
        t.speed(0)
        t.penup()
        self._visualize(self.root, 0, 0, 200, t)
        screen.mainloop()

    def _visualize(self, node, x, y, offset, t):
        if node:
            t.goto(x, y)
            t.write(node.key, align="center", font=("Arial", 12, "normal"))

            if node.left:
                t.goto(x, y)
                t.pendown()
                t.goto(x - offset, y - 50)
                t.penup()
                self._visualize(node.left, x - offset, y - 50, offset / 2, t)

            if node.right:
                t.goto(x, y)
                t.pendown()
                t.goto(x + offset, y - 50)
                t.penup()
                self._visualize(node.right, x + offset, y - 50, offset / 2, t)

def build_tree(values):
    tree = BinarySearchTree()
    for value in values:
        tree.insert(value)
    return tree

# List a
print("Tree from list a:")
a = [49, 38, 65, 97, 60, 76, 13, 27, 5, 1]
tree_a = build_tree(a)
print("Inorder:", tree_a.inorder_traversal())
tree_a.visualize()

# Uncomment these to visualize other trees
# List b
# print("\nTree from list b:")
# b = [149, 38, 65, 197, 60, 176, 13, 217, 5, 11]
# tree_b = build_tree(b)
# print("Inorder:", tree_b.inorder_traversal())
# tree_b.visualize()

# List c
# print("\nTree from list c:")
# c = [49, 38, 65, 97, 64, 76, 13, 77, 5, 1, 55, 50, 24]
# tree_c = build_tree(c)
# print("Inorder:", tree_c.inorder_traversal())
# tree_c.visualize()
