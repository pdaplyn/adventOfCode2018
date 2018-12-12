"""
>>> inputs = {'A':(1,1), 'B':(1,6), 'C':(8,3), 'D':(3,4), 'E':(5,5), 'F':(8,9)}
>>> matrix = bounds([x for x in inputs.values()])
>>> matrix = closest(inputs, matrix)
>>> # print_matrix(matrix)
>>> ids = sizes(matrix)
>>> # ids
>>> biggest(matrix, ids)
17
>>> score(inputs, matrix)
>>> count_score_below(matrix, 32)
16
"""


from advent_util import read_file


def count_score_below(matrix, limit):
    count = 0
    for row in matrix:
        for score in row:
            if score < limit:
                count += 1
    return count


def biggest(matrix, ids):
    ignore = set()
    for x in matrix[0]:
        ignore.add(x)
    for x in matrix[len(matrix)-1]:
        ignore.add(x)
    for row in matrix:
        ignore.add(row[0])
        ignore.add(row[len(row)-1])

    # print("ignoring", ignore)
    for x in ignore:
        ids[x] = 0
    return max(ids.values())


def sizes(matrix):
    sizes = {}
    for row in matrix:
        for id in row:
            if id not in sizes:
                sizes[id] = 1
            else:
                sizes[id] += 1
    return sizes


def score(inputs, matrix):
    for y in range(len(matrix)):
        row = matrix[y]
        for x in range(len(row)):
            score = calc_score(x, y, inputs)
            matrix[y][x] = score


def calc_score(x, y, inputs):
    score = 0
    for coords in inputs.values():
        x_dist = max(x, coords[0]) - min(x, coords[0])
        y_dist = max(y, coords[1]) - min(y, coords[1])
        total = x_dist + y_dist
        score += total
    return score


def closest(inputs, matrix):
    for y in range(len(matrix)):
        row = matrix[y]
        for x in range(len(row)):
            match = closest_coordinate(x, y, inputs)
            matrix[y][x] = match[0]
    return matrix


def closest_coordinate(x, y, inputs):
    item = ("-", [-1,-1])
    distance = 9999999
    for input in inputs.items():
        coords = input[1]
        x_dist = max(x, coords[0]) - min(x, coords[0])
        y_dist = max(y, coords[1]) - min(y, coords[1])
        total = x_dist + y_dist
        if total < distance:
            item = input
            distance = total
        elif total == distance:
            item = (".", [-1,-1])
    return item


def bounds(input):
    # left = input[0][0];
    right = input[0][0];
    # top = input[0][1];
    bottom = input[0][1];
    for [x,y] in input:
        #if x < left:
        #    left = x
        if x > right:
            right = x
        #if y < top:
        #    top = y
        if y > bottom:
            bottom = y

    matrix = [[0] * (right+1) for i in range(bottom+1)]
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print( row )


# inputs = {'A':(1,1), 'B':(1,6), 'C':(8,3), 'D':(3,4), 'E':(5,5), 'F':(8,9)}
def parse_input(inputs):
    ins = {}
    i=0
    for row in inputs:
        i+=1
        coords = [int(x) for x in row.split(', ')]
        ins[i] = coords
    return ins


in_list = read_file("../inputs/input6.txt")
inputs = parse_input(in_list)
print(inputs)
matrix = bounds([x for x in inputs.values()])
#matrix = closest(inputs, matrix)
#ids = sizes(matrix)
#print("size by id", ids)
#largest = biggest(matrix, ids)
#print("largest area is", largest)

score(inputs, matrix)
area_size = count_score_below(matrix, 10000)
print("area with scores below 10000:", area_size)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
