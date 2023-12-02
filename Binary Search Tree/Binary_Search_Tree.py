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

    def recursive_contains(self, value):
        def helper(root):
            if not root:
                return False

            if root.value == value:
                return True

            if root.value > value:
                return helper(root.left)

            return helper(root.right)

        return helper(self.root)

    def recursive_insert(self, value):
        def helper(root):
            if not root:
                return Node(value)

            if root.value > value:
                root.left = helper(root.left)

            elif root.value < value:
                root.right = helper(root.right)

            return root

        self.root = helper(self.root)

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

    def breadth_first_search(self):
        queue = []
        result = []

        queue.append(self.root)

        while len(queue) > 0:
            if queue[0].left:
                queue.append(queue[0].left)

            if queue[0].right:
                queue.append(queue[0].right)

            result.append(queue.pop(0).value)

        return result

    def depth_first_search(self, order='pre'):
        result = []

        def pre_order_traverse(root):
            result.append(root.value)

            if root.left:
                pre_order_traverse(root.left)

            if root.right:
                pre_order_traverse(root.right)

        def post_order_traverse(root):
            if root.left:
                post_order_traverse(root.left)

            if root.right:
                post_order_traverse(root.right)

            result.append(root.value)

        def in_order_traverse(root):
            if root.left:
                in_order_traverse(root.left)

            result.append(root.value)

            if root.right:
                in_order_traverse(root.right)

        if order != 'pre' and order != 'post' and order != 'in':
            raise ValueError

        if self.root:
            if order == 'pre':
                pre_order_traverse(self.root)
            elif order == 'post':
                post_order_traverse(self.root)
            else:
                in_order_traverse(self.root)
        return result


my_tree = BinarySearchTree()
my_tree.recursive_insert(10)
my_tree.recursive_insert(12)
my_tree.recursive_insert(18)
my_tree.recursive_insert(8)
my_tree.recursive_insert(7)
my_tree.recursive_insert(9)

# print(my_tree)
# print(my_tree.recursive_contains(8))

print(my_tree.depth_first_search())
