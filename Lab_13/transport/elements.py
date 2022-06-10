
class Node:

    id = 0

    def __init__(self, data):
        Node.id += 1
        self._id = Node.id
        self._data = data
        self._in_branches = []
        self._out_branches = []
        self._visited = []
        self._completed = False

    def set_in_branch(self, branch):
        self._in_branches.append(branch)

    def set_out_branch(self, branch):
        self._out_branches.append(branch)

    def set_visited(self, node):
        self._visited.append(node)

    def set_completed(self, value):
        self._completed = value

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

    @property
    def completed(self):
        return self._completed

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


class DepthFirstSearch:

    def __init__(self, first, last, nodes, graph):
        self._graph = graph
        self._first = first
        self._last = last
        self._path = []
        self._path_list = []
        self._nodes = nodes
        self._forks = []
        self._isFirst = True
        self._last_fork = None

    def search(self, current=-1):  # TODO: da sistemare

        # Inizializzazione
        if current == -1:
            current = self._first
        if self._isFirst:
            for node in self._nodes:
                node.reset_path()
                self._isFirst = False

        # Creazione percorso
        if current.get_id() not in self._path:
            self._path.append(current.get_id())

        # Tracciamento diramazioni
        if len(current.out_branches) - len(current.visited) > 1 and not current.completed:
            self._forks.append(current)
        elif current in self._forks:
            self._forks.remove(current)
        if len(current.out_branches) - len(current.visited) == 0:
            if len(self._forks) >= 1:
                self._forks.pop().set_completed(True)
            for node in self._nodes:
                if node not in self._forks:
                    node.reset_path()
        self._last_fork = self._forks[-1]

        # # TODO: elimina -----------------------------------
        # print("\nNodo:", current.get_id())
        # try:
        #     print("Ultima diramazione:", self._last_fork.get_id(), self._last_fork)  # TODO: elimina
        # except:
        #     pass
        # print("Percorso:", self._path)
        # list = []
        # for f in self._forks:
        #     list.append(f.get_id())
        # print("Diramazioni:", list)
        # list = []
        # for f in current.out_branches:
        #     list.append(f.get_link())
        # print("Branches:", list)
        # list = []
        # for f in current.visited:
        #     list.append(f.get_id())
        # print("Visited:", list)
        # # TODO: elimina ------------------------------------

        # Raggiunta la meta
        if current == self._last:
            # index = self._path.index(self._forks[-1].get_id())
            index = self._path.index(self._last_fork.get_id())  # --------
            self._path_list.append(self._path)
            self._path = self._path[:index + 1]
            # print("Arrivato")  # TODO: elimina

        # Fine percorso
        elif len(current.out_branches) == 0:
            index = self._path.index(self._last_fork.get_id())  # --------
            self._path = self._path[:index + 1]
            # print("Fine percorso")  # TODO: elimina

        # Continua a cercare
        else:
            out_branches = current.out_branches
            i = 0
            while i < len(out_branches):
                # print("i:", i)  # TODO: elimina
                node = self._graph.get_node_obj(current.out_branches[i].get_link()[1])
                if node not in current.visited:
                    current.set_visited(node)
                    # print(f"{current.get_id()} -> {node.get_id()}")  # TODO: elimina
                    # print("Percorso:", self._path)  # TODO: elimina
                    self.search(node)
                i += 1

    def best_path(self):
        indexes = []
        for path in self._path_list:
            indexes.append(len(path))

        return self._path_list[indexes.index(min(indexes))]