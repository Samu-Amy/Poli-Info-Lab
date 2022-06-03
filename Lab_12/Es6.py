
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
        min = self._head.min(self._head)
        return min

    # TODO: aggiungi metodo di stampa (ordinata ma senza algoritmi di sorting)
    def __repr__(self):
        pass


class Node:

    def __init__(self, data: int) -> None:
        self._data = data
        self._less = None
        self._greater = None

    def get(self):
        return self._data

    def get_less(self):
        return self._less

    def get_all(self):
        string = ""
        string += str(self._data) + ", "
        try:
            string += str(self._less.get()) + ", "
        except AttributeError:
            string += str(self._less) + " "
        try:
            string += str(self._greater.get())
        except AttributeError:
            string += str(self._greater)
        return string

    def __le__(self, other):
        return self._data <= other.get()

    def __gt__(self, other):
        return self._data > other.get()

    def add_node(self, other):
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


node1 = Node(5)
node2 = Node(2)
node3 = Node(10)
node4 = Node(6)
node5 = Node(12)
node6 = Node(1)

tree = BinarySearchTree(node1)
tree.add(node2)
tree.add(node3)
tree.add(node4)
tree.add(node5)
tree.add(node6)


list = tree.get_nodes()

for node in list:
    print(node.get_all())


print(f"\nMinimo: {tree.get_min().get()}")
