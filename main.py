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

    def insert(self, value):
        # first, we make a new node and increase the tree size by 1
        node = Node(value)
        node.parent = None
        node.left = self.nil
        node.right = self.nil
        self.size += 1
        # then, we place the node in the tree according to the value
        x = self.root
        y = None
        while x != self.nil:
            # move down the tree until we reach the target leaf node
            y = x
            if node.value < x.value:
                x = x.left
            else:
                x = x.right

        node.parent = y
        # handle if node is the root element of the tree
        if y == None:
            self.root = node
        # otherwise, link correctly to the parent
        elif node.value < y.value:
            y.left = node
        else:
            y.right = node

        # color the root black
        if node.parent == None:
            node.color = "black"
            return
        # when new node is a red child of the root, need not do any fix
        if node.parent.parent == None:
            return
        # finally, fix the tree from insertion operation
        self.fix(node)

    # def fix(self, node):


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
        elif direction is "right":
            # y's right becomes x's left
            y = x.left
            x.left = y.right
            if y.right != self.nil:
                y.right.parent = x
            # x's parent becomes y's parent
            y.parent = x.parent
            if x.parent is None:
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


file = open("EN-US-Dictionary.txt", "r")
for x in file:
    print(x)
