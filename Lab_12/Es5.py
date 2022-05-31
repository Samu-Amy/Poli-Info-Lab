
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

    def print_string(self):
        string = ''
        if isinstance(self._node.get(), str):
            string += f'\"{self._node.get()}\"'
        else:
            string += str(self._node.get())
        return string

    def __getitem__(self, pos):
        self._node = self._head
        for index in range(pos):
            self._node = self._node.get_next()
        try:
            return self.print_string()
        except AttributeError:
            return "Index incorrect"

    def __repr__(self) -> str:
        string = ''
        self._node = self._head
        while self._node.get_next() is not None:
            string += self.print_string()
            string += ', '
            self._node = self._node.get_next()
        string += self.print_string()
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
print(queue)
queue.append(2)
print(queue)
queue.append("3")
print(queue)
queue.pop()
print(queue)
queue.append("Third")
print(queue)

print()

print(queue[0])
print(queue[1])
print(queue[2])
print(queue[3])
