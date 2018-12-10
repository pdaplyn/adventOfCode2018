"""
>>> test = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
>>> parse_claim(test[0])
{'id': '#1', 'left': 1, 'top': 3, 'width': 4, 'height': 4}
>>> claims = [parse_claim(x) for x in test]
>>> canvas = count_claims(claims)
Canvas size:  7 7
>>> canvas
[[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1, 1], [0, 1, 1, 2, 2, 1, 1], [0, 1, 1, 2, 2, 1, 1], [0, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1]]
>>> overlapping_count(canvas)
4
>>> find_clean_claim(canvas, claims)
'#3'
"""

from advent_util import read_file


def find_clean_claim(canvas, claims):
    for claim in claims:
        right = claim['left'] + claim['width']
        bottom = claim['top'] + claim['height']
        clean = True
        for i in range(claim['left'], right):
            for j in range(claim['top'], bottom):
                if canvas[i][j] > 1:
                    clean = False
        if clean:
            return claim['id']
    return "unknown"


def overlapping_count(canvas):
    count = 0
    for row in canvas:
        for cell in row:
            if cell > 1:
                count += 1
    return count


def count_claims(claims):
    # find canvas size
    canvas_width = 0
    canvas_height = 0
    for claim in claims:
        width = claim['left'] + claim['width']
        canvas_width = max(canvas_width, width)
        height = claim['top'] + claim['height']
        canvas_height = max(canvas_height, height)

    print("Canvas size: ", canvas_width, canvas_height)
    canvas = [[0] * canvas_height for i in range(canvas_width)]
    for claim in claims:
        # print(claim)
        right = claim['left'] + claim['width']
        bottom = claim['top'] + claim['height']
        for i in range(claim['left'], right):
            for j in range(claim['top'], bottom):
                # print("incrementing ", i, j)
                canvas[i][j] += 1

    return canvas


def parse_claim(str):
    [id, details] = str.split(" @ ")
    [position, size] = details.split(": ")
    [left, top] = [int(x) for x in position.split(",")]
    [width, height] = [int(x) for x in size.split("x")]

    claim = {
        "id": id,
        "left": left,
        "top": top,
        "width": width,
        "height": height
    }
    return claim

claim_strings = read_file("../inputs/input3.txt")
claims = [parse_claim(x) for x in claim_strings]
canvas = count_claims(claims)
count = overlapping_count( canvas)
print("number of overlapping cells is", count)

clean_claim = find_clean_claim(canvas, claims)
print("non-overlapping claim is ", clean_claim)

# print("Same letters are ", same_letters)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
