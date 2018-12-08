# advent_util.py


def read_file(filename):
    print("Opening file ", filename)
    input_strings = []
    input_file = open(filename, "r")
    for line in input_file:
        input_strings.append(line)
    return input_strings
