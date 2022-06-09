
class Node:

    id = 0

    def __init__(self, data):
        Node.id += 1
        self._id = Node.id
        self._data = data
        self._in_branches = []
        self._out_branches = []
        self._visited = []

    def set_in_branch(self, branch):
        self._in_branches.append(branch)

    def set_out_branch(self, branch):
        self._out_branches.append(branch)

    def set_visited(self, node):
        self._visited.append(node)

    def reset_path(self):
        self._visited = []

    @property
    def out_branches(self):
        return self._out_branches

    @property
    def in_branches(self):
        return self._in_branches

    @property
    def visited(self):
        return self._visited

    def get(self):
        return self._data

    def get_id(self):
        return self._id


class Branch:

    def __init__(self, weight, from_node, to_node):
        self._weight = weight
        self._from_node = from_node
        self._to_node = to_node

    def get_weight(self):
        return self._weight

    def get_link(self):
        return self._from_node, self._to_node


class Depth_First_Search:

    def __init__(self, first, last, nodes, graph):
        self._graph = graph
        self._first = first
        self._last = last
        self._path = []
        self._path_list = []
        self._nodes = nodes
        self._forks = []
        self._isFirst = True

    def search(self, current=-1):

        # Inizializzazione
        if current == -1:
            current = self._first
        if self._isFirst:
            for node in self._nodes:
                node.reset_path()
                self._first = False

        # Raggiunta la meta
        if current == self._last:
            self._path_list.append(self._path)
            self._path = []

        # Fine percorso
        elif len(current.out_branches) == 0:
            self._path = []  # Reset percorso

        # Continua a cercare
        else:
            out_branches = current.out_branches
            i = 0
            while i < len(out_branches) - 1:
                node = self._graph.get_node_obj(current.out_branches[i].get_link()[1])
                if node in current.visited:
                    i += 1
                else:
                    current.set_visited(node)
                    print(f"Da: {current.get_id()} a: {node.get_id()}")
                    self.search(node)

