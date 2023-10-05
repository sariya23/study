class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, node):
        left_child = node.left
        right_of_left = left_child.right

        # perform rotation
        left_child.right = node
        node.left = right_of_left

        # update heights
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        left_child.height = 1 + max(self.height(left_child.left), self.height(left_child.right))

        return left_child

    def rotate_left(self, node):
        right_child = node.right
        left_of_right = right_child.left

        # perform rotation
        right_child.left = node
        node.right = left_of_right

        # update heights
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        right_child.height = 1 + max(self.height(right_child.left), self.height(right_child.right))

        return right_child

    def insert(self, value):
        def insert_helper(node, value):
            # Base case: node is None, create new node
            if node is None:
                return Node(value)

            # insert node into the appropriate subtree
            if value < node.value:
                node.left = insert_helper(node.left, value)
            else:
                node.right = insert_helper(node.right, value)

            # update height of node
            node.height = 1 + max(self.height(node.left), self.height(node.right))

            # check balance factor and perform rotations as necessary
            balance = self.balance_factor(node)
            if balance > 1 and value < node.left.value:
                return self.rotate_right(node)
            if balance < -1 and value > node.right.value:
                return self.rotate_left(node)
            if balance > 1 and value > node.left.value:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)
            if balance < -1 and value < node.right.value:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)

            return node

        self.root = insert_helper(self.root, value)

    def find(self, value):
        def find_helper(node, value):
            if node is None:
                return None
            if node.value == value:
                return node
            if value < node.value:
                return find_helper(node.left, value)
            else:
                return find_helper(node.right, value)

        return find_helper(self.root, value)

    def display(self, level=0, prefix='   '):
        if self.root is None:
            print('Empty tree')
            return

        def display_helper(node, level, prefix):
            if node is None:
                return
            display_helper(node.right, level + 1, prefix)
            print(prefix * level + '->', node.value, '({})'.format(node.height))
            display_helper(node.left, level + 1, prefix)

        display_helper(self.root, level, prefix)


if __name__ == '__main__':

    a = AVLTree()
    l = [10, 15, 34, 90, 3]


    for i in l:
        a.insert(i)


    a.display()
    print(a.find(34))
