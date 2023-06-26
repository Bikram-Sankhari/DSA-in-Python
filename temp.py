import gc
from binary_tree import BinaryTree
from node_of_binary_tree import NodeOfBinaryTree


class DeletionHelper:
    def __init__(self, root: NodeOfBinaryTree):
        self.depth = 1
        self.node = root


def prev(root: NodeOfBinaryTree) -> DeletionHelper:
    result = DeletionHelper(root.left)
    result.depth += 1

    while result.node.right is not None:
        result.node = result.node.right

    return result


def postr(root: NodeOfBinaryTree) -> DeletionHelper:
    result = DeletionHelper(root.right)

    while result.node.left is not None:
        result.node = result.node.left

    return result


def delete(root: NodeOfBinaryTree, key: int) -> NodeOfBinaryTree:
    if root is None:
        print(f"Key {key} doesn't exists in the Tree")

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


def in_order_traverse(root: NodeOfBinaryTree):
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
delete(tree.root, 50)
in_order_traverse(tree.root)
