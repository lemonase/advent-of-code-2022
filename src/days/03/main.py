import sys

input_file = sys.argv[1]


def get_pri(input_char):
    priority = 0
    if input_char.islower():
        priority = ord(input_char) - 96
    if input_char.isupper():
        priority = ord(input_char) - 38

    return priority


# part 1
def part_one():
    point_sum = 0
    with open(input_file, "r") as f:
        for line in f:
            half = len(line) // 2
            h1 = set(line[:half])
            h2 = set(line[half:])
            inter = h1.intersection(h2)
            common_chars = inter.pop()
            point_sum += get_pri(common_chars)
    print(point_sum)


# part 2
def part_two():
    groups = []
    point_sum = 0

    with open(input_file, "r") as f:
        lines = f.read().splitlines()
        for i, line in enumerate(lines):
            if i % 3 == 0 and i != 0:
                group = lines[i-3:i]
                groups.append(group)

        groups.append(lines[len(lines)-3:len(lines)])

    for group in groups:
        u = set.intersection(set(group[0]), set(group[1]), set(group[2]))
        c = u.pop()
        point_sum += get_pri(c)

    print(point_sum)


part_one()
part_two()
