"""
>>> input = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
>>> node = parse(input)
>>> len(node.children)
2
>>> len(node.metadata)
3
>>> node.sum_meta()
138
>>> node.value()
66
"""


from advent_util import read_file


class Node:
    def __init__(self, child_count, meta_count):
        self.child_count = child_count
        self.meta_count = meta_count
        self.children = []
        self.metadata = []

    def sum_meta(self):
        sum_of_meta = sum(self.metadata)
        for child in self.children:
            sum_of_meta += child.sum_meta()
        return sum_of_meta

    def value(self):
        if len(self.children) == 0:
            return self.sum_meta()
        else:
            sub_total = 0
            for child_index in self.metadata:
                if child_index > 0 and child_index <= len(self.children):
                    child = self.children[child_index-1]
                    sub_total += child.value()
            return sub_total


def parse(input):
    inputs = [int(x) for x in input.strip().split(" ")]
    inputs.reverse()
    node = read_node(inputs)
    return node


def read_node(inputs):
    child_count = inputs.pop()
    meta_count = inputs.pop()
    node = Node(child_count, meta_count)

    for i in range(child_count):
        child = read_node(inputs)
        node.children.append(child)

    for i in range(meta_count):
        meta = inputs.pop()
        node.metadata.append(meta)

    return node


input = read_file("../inputs/input8.txt")
node = parse(input[0])
total = node.sum_meta()
print("Sum of metadata is", total)
v = node.value()
print("Node value is", v)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
