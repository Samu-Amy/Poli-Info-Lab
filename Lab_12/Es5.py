


class FirstInFirstOut:

    def __init__(self, object) -> None:
        self._node = Node(object)
        self._head = self._node
        self._tail = self._node

    def append(self, object) -> None:
        self._node = Node(object)
        self._tail.set_next(self._node)
        self._tail = self._node

    def pop(self):
        self._node = self._head
        self._head = self._node.get_next()
        self._node.reset_next()
        return self._node.get()

    def __repr__(self) -> str:
        string = ''
        self._node = self._head
        hasNext = self._node.get_next() != None
        while hasNext:
            if isinstance(self._node.get(), str):
                string += f'\"{self._node.get()}\"'
            else:
                string += str(self._node.get())
            string += ", "
            self._node = self._node.get_next()
        return string


class Node:

    def __init__(self, object) -> None:
        self._object = object
        self._next = None

    def get(self):
        return self._object

    def set_next(self, other: "Node") -> None:
        self._next = other

    def get_next(self) -> "Node":
        return self._next

    def reset_next(self):
        self._next = None


queue = FirstInFirstOut("First")
# print(queue)
queue.append(2)
# print(queue)
queue.append("3")
queue.pop()
print(queue)

