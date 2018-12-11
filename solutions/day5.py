"""
>>> reduce("aA")
''
>>> reduce("abBA")
''
>>> reduce("aabAAB")
'aabAAB'
>>> reduce("dabAcCaCBAcCcaDA")
'dabCBAcaDA'
>>> smallest("dabAcCaCBAcCcaDA")
4
"""


import string
from advent_util import read_file


def reduce(input):
    letters = []
    for x in input:
        last_index = len(letters) - 1
        y = x.swapcase()

        if last_index>=0 and letters[last_index] == y:
            letters.pop()
        else:
            letters.append(x)

    return "".join(letters)


def smallest(input):
    reduced_size = len(input)
    for char in string.ascii_lowercase:
        replaced = input.replace(char, "").replace(char.swapcase(), "")
        reduced = reduce(replaced)
        if len(reduced) < reduced_size:
            reduced_size = len(reduced)
    return reduced_size


input = read_file("../inputs/input5.txt")
polymers = input[0].rstrip()
print("input length:", len(polymers))
reduced = reduce(polymers)
print("reduced polymer:", len(reduced), "'"+reduced+"'")

print("smallest after removing one:", smallest(polymers))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
