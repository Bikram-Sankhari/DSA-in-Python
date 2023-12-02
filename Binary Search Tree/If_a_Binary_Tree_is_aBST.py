from typing import Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root: Optional[Node] = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True

        temp = self.root
        while True:
            if temp.value == value:
                return False

            if temp.value < value:
                if not temp.right:
                    temp.right = new_node
                    return True
                temp = temp.right

            else:
                if not temp.left:
                    temp.left = new_node
                    return True

                temp = temp.left

    def contains(self, value):
        temp = self.root

        while temp:
            if temp.value == value:
                return True
            elif temp.value > value:
                temp = temp.left
            else:
                temp = temp.right

        return False

    def __str__(self):
        def inner_print(root):
            if root:
                inner_print(root.left)
                print(root.value, end=' ')
                inner_print(root.right)

        inner_print(self.root)
        return ''

    def delete(self, value):
        def inner_delete(root, inner_value):
            if root:
                if root.value > inner_value:
                    root.left = inner_delete(root.left, inner_value)

                elif root.value < inner_value:
                    root.right = inner_delete(root.right, inner_value)

                else:
                    if not root.left:
                        return root.right
                    if not root.right:
                        return root.left
                    else:
                        temp = root.left
                        while temp.right:
                            temp = temp.right

                        root.value = temp.value
                        root.left = inner_delete(root.left, temp.value)

            return root

        self.root = inner_delete(self.root, value)


temp = None


def is_bst(tree: BinarySearchTree) -> bool:
    def inner_is_bst(root) -> bool:
        global temp
        if not root:
            return True

        if not inner_is_bst(root.left):
            return False

        if temp and root.value <= temp.value:
            return False

        temp = root
        if not inner_is_bst(root.right):
            return False

        return True

    return inner_is_bst(tree.root)


my_tree = BinarySearchTree()
my_tree.insert(10)
left_node = Node(9)
right_node = Node(11)

my_tree.root.left = right_node
my_tree.root.right = left_node

print(is_bst(my_tree))
