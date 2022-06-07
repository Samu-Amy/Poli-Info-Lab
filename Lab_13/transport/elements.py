
class Node:

    id = 0

    def __init__(self, data):
        Node.id += 1
        self._id = Node.id
        self._data = data
        self._in_branches = []
        self._out_branches = []

    def set_in_branch(self, branch):
        self._in_branches.append(branch)

    def set_out_branch(self, branch):
        self._out_branches.append(branch)

    def get_out_branches(self):
        return self._out_branches

    def get_in_branches(self):
        return self._in_branches

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
