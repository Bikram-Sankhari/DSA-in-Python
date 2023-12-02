import gc
from binary_tree import BinaryTree
from node_of_binary_tree import NodeOfBinaryTree


class DeletionHelper:
    def __init__(self):
        self.node = None
        self.depth = 0


def prev(root: NodeOfBinaryTree) -> DeletionHelper:
    temp = DeletionHelper()
    temp.node = root.left
    temp.depth += 1

    while not temp.node.right is None:
        temp.node = temp.node.right
        temp.depth += 1

    return temp


def postr(root: NodeOfBinaryTree) ->DeletionHelper:
    temp = DeletionHelper()
    temp.node = root.right
    temp.depth += 1

    while not temp.node.left is None:
        temp.node = temp.node.left
        temp.depth += 1

    return temp


def delete(root: NodeOfBinaryTree, key: int) -> NodeOfBinaryTree:
    if root is None:
        print(f"Element {key} doesn't exists in the tree")

    elif root.data > key:
        root.left = delete(root.left, key)

    elif root.data < key:
        root.right = delete(root.right, key)

    else:
        if root.left is None:
            temp = root.right
            del root
            gc.collect()
            return temp

        if root.right is None:
            temp = root.left
            del root
            gc.collect()
            return temp

        pre = prev(root)
        post = postr(root)

        if pre.depth <= post.depth:
            root.data = pre.node.data
            root.left = delete(root.left, pre.node.data)
        else:
            root.data = post.node.data
            root.right = delete(root.right, post.node.data)

    return root


def in_order_traverse(root:NodeOfBinaryTree):
    if not root is None:
        in_order_traverse(root.left)
        print(root.data, end=" ")
        in_order_traverse(root.right)


#                           50
#                    _______ | ________
#                   |                  |
#                   25                 90
#               ____ | ____        ____ | ____
#              |           |      |           |
#             20           30                130
#                                        ____ | _____
#                                       |            |
#                                      100           150

tree = BinaryTree()
in_order_traverse(tree.root)

print("\n---------------------After Deletion---------------------")
delete(tree.root, 90)
in_order_traverse(tree.root)

