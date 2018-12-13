"""
>>> inputs = read_file("../inputs/input7-test.txt")
Opening file  ../inputs/input7-test.txt
>>> [dependants, dependencies] = graph(inputs)
>>> start = find_start(dependants)
>>> start
['C']
>>> traverse(start, dependants, dependencies)
['C', 'A', 'B', 'D', 'F', 'E']
"""


from advent_util import read_file


def traverse(start, dependants, dependencies):
    print(dependants)
    print(dependencies)
    order = []
    ready = start
    while len(ready)>0:
        print("Order", order )
        print("Ready", ready )
        ready.sort(reverse=True)
        next = ready.pop()
        order += next
        print("next", next)
        if next in dependants:
            for dependant in dependants[next]:
                if dependant in order:
                    continue
                if dependant in ready:
                    continue
                check = []
                if dependant in dependencies:
                    check = dependencies[dependant]
                if set(order).issuperset(set(check)):
                    ready.append(dependant)
    return order


def find_start(nodes):
    keys = []
    for key in nodes.keys():
        found = False
        for dependants in nodes.values():
            if key in dependants:
                found = True
                break
        if not found:
            keys.append(key)
    return keys


def graph(inputs):
    dependencies = {}
    dependants = {}
    for input in inputs:
        [a, before, b, c, d, e, f, after, g, h] = input.strip().split(" ")
        if after in dependencies.keys():
            dependencies[after] += before
        else:
            dependencies[after] = [before]
        if before in dependants.keys():
            dependants[before] += after
        else:
            dependants[before] = [after]
    return [dependants,dependencies]


inputs = read_file("../inputs/input7.txt")
[dependants, dependencies] = graph(inputs)
start = find_start(dependants)
order = traverse(start, dependants, dependencies)
print("Step order: ", "".join(order))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
