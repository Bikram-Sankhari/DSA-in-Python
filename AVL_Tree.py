import gc


class NodeOfAVLTree:
    def __init__(self, data):
        self.data = data
        self.height = 1
        self.left: NodeOfAVLTree = None
        self.right: NodeOfAVLTree = None


def in_order_traverse(root: NodeOfAVLTree):
    if root is not None:
        in_order_traverse(root.left)
        print(root.data, end=" ")
        in_order_traverse(root.right)


def get_height(root: NodeOfAVLTree) -> int:
    if root is None:
        return 0
    return root.height


def update_height(root: NodeOfAVLTree):
    lh = get_height(root.left)
    rh = get_height(root.right)

    root.height = max(lh, rh) + 1


def balance_factor(root: NodeOfAVLTree) -> int:
    lh = get_height(root.left)
    rh = get_height(root.right)

    return lh - rh


def rotate_right(root: NodeOfAVLTree) -> NodeOfAVLTree:
    result = root.left
    temp = root.left.right
    root.left.right = root
    root.left = temp

    update_height(root)
    update_height(result)

    return result


def rotate_left(root: NodeOfAVLTree) -> NodeOfAVLTree:
    result = root.right
    temp = root.right.left
    root.right.left = root
    root.right = temp

    update_height(root)
    update_height(result)

    return result


def apply_rotation(root: NodeOfAVLTree) -> NodeOfAVLTree:
    bf = balance_factor(root)

    if bf > 1:
        if balance_factor(root.left) == -1:
            root.left = rotate_left(root.left)

        return rotate_right(root)

    elif bf < -1:
        if balance_factor(root.right) == 1:
            root.right = rotate_right(root.right)

        return rotate_left(root)
    return root


def insert(root: NodeOfAVLTree, key: int) -> NodeOfAVLTree:
    if root is None:
        return NodeOfAVLTree(key)

    elif root.data > key:
        root.left = insert(root.left, key)

    elif root.data < key:
        root.right = insert(root.right, key)

    else:
        print(f"key {key} already exists in the Tree")

    update_height(root)
    return apply_rotation(root)


def delete(root: NodeOfAVLTree, key: int) -> NodeOfAVLTree:
    if root is None:
        print(f"key {key} is not present in the Tree")
    elif root.data > key:
        root.left = delete(root.left, key)
    elif root.data < key:
        root.right = delete(root.right, key)
    else:
        if root.right is None:
            result = root.left
            del root
            gc.collect()
            return result

        if root.left is None:
            result = root.right
            del root
            gc.collect()
            return result

        temp = root.left
        while temp.right is not None:
            temp = temp.right

        root.data = temp.data
        root.left = delete(root.left, temp.data)

    update_height(root)
    return apply_rotation(root)


"""
                                      40
                           ____________|____________
                          |                         |
                          20                       70
                       ___|___             _________|_________
                      |       |           |                   |
                      10      30          50                  80
                   ___|____           ____|_____         _____|______
                  |                  |          |                    |
                  5                  45         60                   90

"""

root = NodeOfAVLTree(10)
root = insert(root, 20)
root = insert(root, 30)
root = insert(root, 40)
root = insert(root, 50)
root = insert(root, 60)
root = insert(root, 70)
root = insert(root, 80)
root = insert(root, 90)
root = insert(root, 5)

in_order_traverse(root)
print(f"\n{root.left.data}")
print("---------------------------------------After Deletion---------------------------------------")
root = delete(root, 30)
in_order_traverse(root)
print(f"\n{root.left.data}")
