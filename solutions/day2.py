"""
>>> test = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
>>> [twos(x) for x in test]
[0, 1, 1, 0, 1, 1, 0]
>>> [threes(x) for x in test]
[0, 1, 0, 1, 0, 0, 1]
>>> part2_test = ["abcde","fghij","klmno","pqrst","fguij","axcye","wvxyz"]
>>> similar(part2_test)
['fghij', 'fguij']
"""

from advent_util import read_file


def char_count(id):
    char_map = {}
    for char in id:
        if char in char_map:
            char_map[char] = char_map[char] + 1
        else:
            char_map[char] = 1;
    return char_map


def twos(id):
    if 2 in char_count(id).values():
        return 1
    return 0


def threes(id):
    if 3 in char_count(id).values():
        return 1
    return 0


def similar(ids):
    for id1 in ids:
        for id2 in ids:
            if id1 == id2:
                continue

            diff_count = 0
            for i in range(len(id1)):
                if id1[i] != id2[i]:
                    diff_count += 1
                if diff_count > 1:
                    break
            if diff_count == 1:
                return [id1,id2]


def same(id1, id2):
    same = ""
    for i in range(len(id1)):
        if id1[i] == id2[i]:
            same += id1[i]
    return same


ids = read_file("../inputs/input2.txt")

two_count = 0;
three_count = 0;
for id in ids:
    char_map = char_count(id)
    if 2 in char_map.values():
        two_count += 1
    if 3 in char_map.values():
        three_count += 1

print("Checksum is ", two_count*three_count)

similar_ids = similar(ids)
print("Similar ids are ", similar_ids)

same_letters = same(similar_ids[0], similar_ids[1])
print("Same letters are ", same_letters)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
