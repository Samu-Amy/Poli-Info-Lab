
class Node:

    id = 0

    def __init__(self, data):
        self._id = Node.id
        Node.id += 1
        self._data = data


n1 = Node(25)
n2 = Node(50)
n3 = Node(75)

print(n1._id)
