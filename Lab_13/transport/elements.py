
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

    def get(self):
        return self._data

    def get_id(self):
        return self._id

    @property
    def out_branches(self):
        return self._out_branches

    @property
    def in_branches(self):
        return self._in_branches

    @property
    def visited(self):
        return self._visited


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
        self._previous = None
        self._arrived = False
        self._pivot = []

    def search2(self, node=-1, last=-1, pivot=None, branch=None):

        # Inizializzazione
        if node == -1:
            node = self._first
        if last == -1:
            last = self._last

        self._arrived = False
        self._path.append(node)

        print()
        print("Nodo:", node.get_id())
        if pivot is not None:
            print("Prima:", pivot.get_id())  # TODO: elimina
        print("Percorso:", end=" ")
        for m in self._path:
            print(m.get_id(), end=", ")
        print()

        # Raggiunta la meta
        if node == last:
            print("Arrivato")  # TODO: elimina
            self._path_list.append(self._path)
            self._arrived = True

        # Fine percorso
        elif len(node.out_branches) == 0:
            print("Fine percorso")  # TODO: elimina
            self._arrived = True

        # Continua il percorso
        elif len(node.out_branches) > 0:
            print("Continua")  # TODO: elimina
            for branch in node.out_branches:
                n = self._graph.get_node_obj(branch.get_link()[1])
                node.set_visited(n)
                if len(node.out_branches) > 1:
                    pivot = self._graph.get_node_obj(branch.get_link()[0])
                #     if pivot not in self._pivot:
                #         self._pivot.append(pivot)
                #         print("Pivot:", end=" ")
                #         for m in self._pivot:
                #             print(m.get_id(), end=", ")
                #         print()
                # if len(node.out_branches) - len(node.visited) == 0:
                #     print("Visitati:", end=" ")
                #     for m in node.visited:
                #         print(m.get_id(), end=", ")
                #     print()
                #     index = self._pivot.index(pivot)
                #     try:
                #         pivot = self._pivot[index - 1]
                #     except IndexError:
                #         pass
                    print("Prima:", pivot.get_id())  # TODO: elimina
                self._arrived = False
                print("Funzione:", n.get_id(), pivot.get_id(), branch.get_link())
                self.search2(n, last, pivot, branch)

        if self._arrived:
            self._arrived = False
            print("Prima:", pivot.get_id())  # TODO: elimina
            index = self._path.index(pivot)
            self._path = self._path[:index + 1]
            print(index, len(self._path))
            print("Percorso:", end=" ")
            for m in self._path:
                print(m.get_id(), end=", ")
            print()

    def best_path(self):
        indexes = []
        for path in self._path_list:
            indexes.append(len(path))

        return self._path_list[indexes.index(min(indexes))]


#   def search(self, current=-1):
#
#     # Inizializzazione
#     if current == -1:
#         current = self._first
#     if self._isFirst:
#         for node in self._nodes:
#             node.reset_path()
#             self._isFirst = False
#
#     # Creazione percorso
#     if current.get_id() not in self._path:
#         self._path.append(current.get_id())
#
#     # Tracciamento diramazioni
#     if len(current.out_branches) - len(current.visited) > 1 and not current.completed:
#         self._forks.append(current)
#     elif current in self._forks:
#         self._forks.remove(current)
#     if len(current.out_branches) - len(current.visited) == 0:
#         if len(self._forks) >= 1:
#             self._forks.pop().set_completed(True)
#         for node in self._nodes:
#             if node not in self._forks:
#                 node.reset_path()
#     self._last_fork = self._forks[-1]
#
#     # TODO: elimina -----------------------------------
#     print("\nNodo:", current.get_id())
#     try:
#         print("Ultima diramazione:", self._last_fork.get_id(), self._last_fork)  # TODO: elimina
#     except:
#         pass
#     print("Percorso:", self._path)
#     list = []
#     for f in self._forks:
#         list.append(f.get_id())
#     print("Diramazioni:", list)
#     list = []
#     for f in current.out_branches:
#         list.append(f.get_link())
#     print("Branches:", list)
#     list = []
#     for f in current.visited:
#         list.append(f.get_id())
#     print("Visited:", list)
#     # TODO: elimina ------------------------------------
#
#     # Raggiunta la meta
#     if current == self._last:
#         # index = self._path.index(self._forks[-1].get_id())
#         index = self._path.index(self._last_fork.get_id())  # --------
#         self._path_list.append(self._path)
#         self._path = self._path[:index + 1]
#         print("Arrivato")  # TODO: elimina
#
#     # Fine percorso
#     elif len(current.out_branches) == 0:
#         index = self._path.index(self._last_fork.get_id())  # --------
#         self._path = self._path[:index + 1]
#         print("Fine percorso")  # TODO: elimina
#
#     # Continua a cercare
#     else:
#         out_branches = current.out_branches
#         i = 0
#         while i < len(out_branches):
#             print("i:", i)  # TODO: elimina
#             node = self._graph.get_node_obj(current.out_branches[i].get_link()[1])
#             if node not in current.visited:
#                 current.set_visited(node)
#                 print(f"{current.get_id()} -> {node.get_id()}")  # TODO: elimina
#                 print("Percorso:", self._path)  # TODO: elimina
#                 self.search(node)
#             i += 1


    # def search2_old(self, node=-1, last=-1):
    #
    #     # Inizializzazione
    #     if node == -1:
    #         node = self._first
    #     if last == -1:
    #         last = self._last
    #
    #     self._path.append(node)
    #
    #     # print("Nodo:", node.get_id())
    #     # print("Ultimo:", last.get_id())
    #     # print("Percorso:", end=" ")
    #     # for n in self._path:
    #     #     print(n.get_id(), end=", ")
    #     # print("\n")
    #
    #     # Raggiunta la meta
    #     if node == last:
    #         # print("Arrivato")  # TODO: elimina
    #         # print("Percorso:", end=" ")
    #         # for n in self._path:
    #         #     print(n.get_id(), end=", ")
    #         # print("\n")
    #         self._path_list.append(self._path)
    #         index = self._path.index(self._pivot)
    #         self._path = self._path[:index + 1]
    #         print(index, len(self._path[:index + 1]), len(self._path))
    #
    #     # Fine percorso
    #     elif len(node.out_branches) == 0:
    #         # print("Fine percorso")  # TODO: elimina
    #         # print("Percorso:", end=" ")
    #         # for n in self._path:
    #         #     print(n.get_id(), end=", ")
    #         # print("\n")
    #         index = self._path.index(self._pivot)
    #         self._path = self._path[:index + 1]
    #         print(index, len(self._path[:index + 1]), len(self._path))
    #
    #     # Continua il percorso
    #     elif len(node.out_branches) > 1:
    #         self._pivot = node
    #         for branch in node.out_branches:
    #             n = self._graph.get_node_obj(branch.get_link()[1])
    #             self.search2(n, last)
    #
    #     # print("EEEEEEEEEEEEEEEEEEEEEEEEE")
    #     #
    #     # for i in range(len(self._path_list)):
    #     #     for j in self._path_list[i]:
    #     #         print(j.get_id(), end=", ")
    #     #     print()
    #     #
    #     # print("Pivot:", self._pivot.get_id())
