
class BinarySearchTree:

    def __init__(self, node) -> None:
        self._nodes = []
        self._head = node
        self._nodes.append(node)

    def add(self, node):
        self._head.add_node(node)
        self._nodes.append(node)

    def get_nodes(self):
        return self._nodes

    def get_min(self):
        minimum = self._head.min(self._head)
        return minimum

    # TODO: aggiungi metodo di stampa (ordinata ma senza algoritmi di sorting)
    def __repr__(self):
        datas = []
        minimum = self.get_min()
        datas.append(minimum.get())
        datas.append(minimum.get_previous().get())
        minimum.get_greater()
        string = ""
        for value in datas:
            string += str(value)
            print(value)
        return string


class Node:

    def __init__(self, data: int) -> None:
        self._data = data
        self._less = None
        self._greater = None
        self._previous = None

    def set_previous(self, node):
        self._previous = node

    def get(self):
        return self._data

    def get_less(self):
        return self._less

    def get_greater(self):
        return self._greater

    def get_previous(self):
        return self._previous

    def get_all(self):
        string = ""
        string += str(self._data) + ", "
        try:
            string += str(self._less.get()) + ", "
        except AttributeError:
            string += "N, "
        try:
            string += str(self._greater.get()) + ", "
        except AttributeError:
            string += "N, "
        try:
            string += str(self._previous.get())
        except AttributeError:
            string += str(self._previous)
        return string

    def __le__(self, other):
        return self._data <= other.get()

    def __gt__(self, other):
        return self._data > other.get()

    def add_node(self, other):
        other.set_previous(self)
        if other <= self:
            if self._less is None:
                self._less = other
            else:
                self._less.add_node(other)
        else:
            if self._greater is None:
                self._greater = other
            else:
                self._greater.add_node(other)

    def min(self, node):
        if node.get_less() is not None:
            return self.min(node.get_less())
        else:
            return node

    def to_max(self, node, values):
        if node.get_greater() is not None:
            return self.to_max(node.get_greater(), values)
        else:
            return node


node1 = Node(10)
node2 = Node(5)
node3 = Node(2)
node4 = Node(6)
node5 = Node(15)
node6 = Node(1)
node7 = Node(12)
node8 = Node(18)
node9 = Node(16)
node10 = Node(8)

tree = BinarySearchTree(node1)
tree.add(node2)
tree.add(node3)
tree.add(node4)
tree.add(node5)
tree.add(node6)
tree.add(node7)
tree.add(node8)
tree.add(node9)
tree.add(node10)


list = tree.get_nodes()

for node in list:
    print(node.get_all())


print(f"\nMinimo: {tree.get_min().get()}")

print(tree)
