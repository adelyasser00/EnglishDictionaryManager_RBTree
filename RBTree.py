class Node:
    def __init__(self, value):
        self.value = value
        self.color = "red"
        self.left = None
        self.right = None
        self.parent = None


class RBTree:
    def __init__(self):
        self.nil = Node(0)
        self.nil.color = "black"
        self.nil.left = None
        self.nil.right = None
        self.size = 0
        self.root = self.nil

    def height(self, node):
        if node == self.nil:
            return 0
        else:
            return max(self.height(node.left), self.height(node.right)) + 1

    # Method has problems, fix later
    def inOrderTraversal(self, node):
        if node != self.nil:
            self.inOrderTraversal(node.left)
            print(node.value)
            self.inOrderTraversal(node.right)

    def insert(self, value):
        # first, we make a new node and increase the tree size by 1
        node = Node(value)
        node.parent = None
        node.left = self.nil
        node.right = self.nil
        self.size += 1
        # then, we place the node in the tree according to the value
        x = self.root
        y = self.nil
        while x != self.nil:
            # move down the tree until we reach the target leaf node
            y = x
            if node.value.lower() < x.value.lower():
                x = x.left
            else:
                x = x.right

        node.parent = y
        # handle if node is the root element of the tree
        if y == self.nil:
            self.root = node
        # otherwise, link correctly to the parent
        elif node.value.lower() < y.value.lower():
            y.left = node
        else:
            y.right = node

        # color the root black
        if node.parent == self.nil:
            node.color = "black"
            return
        # when new node is a red child of the root, need not do any fix
        if node.parent.parent == self.nil:
            return
        # finally, fix the tree from insertion operation
        self.fix(node)

    def fix(self, node):
        while node.parent.color == "red":
            # handle if left subtree
            if node.parent is node.parent.parent.left:
                uncle = node.parent.parent.right
                # Case 1: red uncle. Recolor parent, uncle and grandparent
                if uncle.color == "red":
                    node.parent.color = uncle.color = "black"
                    node.parent.parent.color = "red"
                    # After recoloring, recursively check the grandparent node for any tree fixes
                    node = node.parent.parent
                    if node.parent.parent == self.nil:
                        return
                else:
                    # Case 2: black uncle, triangle case, rotate parent and switch to case 3
                    if node is node.parent.right:
                        node = node.parent
                        self.rotate(node, "left")

                    # Case 3: black uncle, line case, recolor parent&grandparent then rotate grandparent
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.rotate(node.parent.parent, "right")

            # handle if right subtree
            else:
                uncle = node.parent.parent.left
                # Case 1: red uncle. Recolor parent, uncle and grandparent
                if uncle.color == "red":
                    node.parent.color = uncle.color = "black"
                    node.parent.parent.color = "red"
                    # After recoloring, recursively check the grandparent node for any tree fixes
                    node = node.parent.parent
                    if node.parent.parent == self.nil:
                        return
                else:
                    # Case 2: black uncle, triangle case, rotate parent and switch to case 3
                    if node is node.parent.left:
                        node = node.parent
                        self.rotate(node, "right")

                    # Case 3: black uncle, line case, recolor parent&grandparent then rotate grandparent
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.rotate(node.parent.parent, "left")

    def rotate(self, x, direction):
        # For left rotation:
        if direction == "left":
            # y's left becomes x's right
            y = x.right
            x.right = y.left
            if y.left != self.nil:
                y.left.parent = x
            # x's parent becomes y's parent
            y.parent = x.parent
            if x.parent is None:
                self.root = y
            elif x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y
            # x is now y's left
            y.left = x
            x.parent = y

        # for right rotation:
        elif direction == "right":
            # y's right becomes x's left
            y = x.left
            x.left = y.right
            if y.right != None:
                y.right.parent = x
            # x's parent becomes y's parent
            y.parent = x.parent
            if x.parent is self.nil:
                self.root = y
            elif x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y
            # x is now y's right
            y.right = x
            x.parent = y

        else:
            # if specified direction is incorrect, return.
            return