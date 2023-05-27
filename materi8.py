class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def min_value_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def max_value_node(self, current_node):
        while current_node.right is not None:
            current_node = current_node.right
        return current_node.value

    def average_value(self):
        if self.root is None:
            return 0
        data = [self.root]
        jumlah_value = 0
        total_node = 0

        while data:
            new_node = data.pop(0)
            jumlah_value += new_node.value
            total_node += 1

            if new_node.left:
                data.append(new_node.left)
            if new_node.right:
                data.append(new_node.right)

        return jumlah_value / total_node


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print('minimum value in Tree: ')
print(my_tree.min_value_node(my_tree.root))
print('maximum value in Tree: ')
print(my_tree.max_value_node(my_tree.root))

print('Average value in tree: ')
print(my_tree.average_value())
