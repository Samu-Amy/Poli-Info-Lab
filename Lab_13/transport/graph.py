import abc
from abc import ABC
from typing import Any, Set, List
from transport.elements import Node, Branch, DepthFirstSearch


class Graph(ABC):

    def __init__(self):
        pass

    @abc.abstractmethod
    def add_node(self, value: Any) -> int:
        pass

    @abc.abstractmethod
    def add_edge(self, value: Any, from_id: int, to_id: int) -> None:
        pass

    @abc.abstractmethod
    def get_node(self, node_id: int) -> Any:
        pass

    @abc.abstractmethod
    def get_edge(self, from_id: int, to_id: int) -> Any:
        pass

    @abc.abstractmethod
    def is_connected(self, from_id: int, to_id: int) -> bool:
        pass

    @abc.abstractmethod
    def get_parents(self, node_id: int) -> Set[int]:
        pass

    @abc.abstractmethod
    def get_children(self, node_id: int) -> Set[int]:
        pass

    @abc.abstractmethod
    def find_path(self, from_id: int, to_id: int) -> List[int]:
        pass


class DirectedGraph(Graph):

    def __init__(self):
        super().__init__()
        self._node = None
        self._nodes = []
        self._branch = None
        self._branches = []

    def add_node(self, value: Any) -> int:
        self._node = Node(value)
        self._nodes.append(self._node)
        return self._node.get_id()

    def add_edge(self, value: Any, from_id: int, to_id: int) -> None:
        self._branch = Branch(value, from_id, to_id)
        self._branches.append(self._branch)
        out_node = self.get_node_obj(from_id)
        out_node.set_out_branch(self._branch)
        in_node = self.get_node_obj(to_id)
        in_node.set_in_branch(self._branch)

    def get_node_obj(self, node_id):
        for node in self._nodes:
            if node.get_id() == node_id:
                self._node = node
                break
        return self._node

    def get_node(self, node_id: int) -> Any:
        for node in self._nodes:
            if node.get_id() == node_id:
                self._node = node
                break
        return self._node.get()

    def get_edge(self, from_id: int, to_id: int) -> Any:
        for branch in self._branches:
            if branch.get_link() == (from_id, to_id):
                self._branch = branch
                break
        return self._branch.get_weight()

    def is_connected(self, from_id: int, to_id: int) -> bool:
        found = False
        for branch in self._branches:
            if branch.get_link() == (from_id, to_id):
                found = True
                break
        return found

    def __len__(self):
        return len(self._nodes)

    def get_parents(self, node_id: int) -> Set[int]:
        self._node = self.get_node_obj(node_id)
        ids = set()
        for branch in self._node.in_branches:
            ids.add(branch.get_link()[0])
        return ids

    def get_children(self, node_id: int) -> Set[int]:
        self._node = self.get_node_obj(node_id)
        ids = set()
        for branch in self._node.out_branches:
            ids.add(branch.get_link()[1])
        return ids

    def find_path(self, from_id: int, to_id: int) -> List[int]:
        dfs = DepthFirstSearch(self.get_node_obj(from_id), self.get_node_obj(to_id), self._nodes, self)
        # dfs.search()
        dfs.search2()

        # return dfs.best_path()



class GraphCreator:
    def __init__(self):
        raise NotImplementedError

    @staticmethod
    def get_empty_graph() -> Graph:
        return DirectedGraph()


# TODO: elimina
graph = GraphCreator.get_empty_graph()
n1 = graph.add_node(5)
n2 = graph.add_node(15)
n3 = graph.add_node(25)
n4 = graph.add_node(50)
n5 = graph.add_node(75)
n6 = graph.add_node(100)
n7 = graph.add_node(125)
b1 = graph.add_edge(1, 1, 2)
b2 = graph.add_edge(2, 1, 3)
b3 = graph.add_edge(6, 1, 5)
b4 = graph.add_edge(5, 2, 3)
b5 = graph.add_edge(2, 2, 4)
b6 = graph.add_edge(6, 3, 5)
b7 = graph.add_edge(6, 3, 6)
b8 = graph.add_edge(6, 3, 7)
b9 = graph.add_edge(6, 4, 5)
b10 = graph.add_edge(6, 5, 6)

# print("Id primo nodo:", n1, end="; ")
# print("contenuto secondo nodo:", graph.get_node(2))
# print("Peso collegamento tra 1 e 3:", graph.get_edge(1, 3))
# print("Il nodo 3 ?? connesso al nodo 1?", graph.is_connected(3, 1))
# print("Il nodo 2 ?? connesso al nodo 3?", graph.is_connected(2, 3))
# print(len(graph))
# print(graph.get_node_obj(2).out_branches[0].get_link())
# print(graph.get_node_obj(2).out_branches[0].get_link())
# l = graph.get_node_obj(3).in_branches
# print(l[0].get_link(), l[1].get_link())
# print(graph.get_children(1))
#
# print(graph.get_node_obj(n1).visited)

graph.find_path(1, 6)
# print(graph.find_path(1, 5))
