"""
>>> test = ["+1", "+1", "+1"]
>>> calc_frequency(test)
[0, 1, 2, 3]
>>> test = ["+1", "+1", "-2"]
>>> calc_frequency(test)
[0, 1, 2, 0]
>>> test = ["-1", "-2", "-3"]
>>> calc_frequency(test)
[0, -1, -3, -6]
>>> test = ["+1", "-2", "+3", "+1"]
>>> calc_frequency(test)
[0, 1, -1, 2, 3]
>>> find_first_repeated( test )
2
"""

from advent_util import read_file

def calc_frequency(input_changes):
    changes = [int(x) for x in input_changes]

    frequency = 0
    frequencies = [ ]
    frequencies.append(frequency)

    for change in changes:
        frequency += change
        frequencies.append(frequency)

    return frequencies


def find_first_repeated(input_changes):
    changes = [int(x) for x in input_changes]

    frequency = 0
    frequencies = {
        str(frequency): 1
    }

    while 1:
        for change in changes:
            frequency += change
            if str(frequency) in frequencies:
                return frequency
            frequencies[str(frequency)] = 1


input_changes = read_file("../inputs/input1.txt")
frequency_results = calc_frequency(input_changes)
print("Final frequency is ", frequency_results[-1])

first_repeated = find_first_repeated(input_changes)
print("First repeated frequency is ", first_repeated)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
