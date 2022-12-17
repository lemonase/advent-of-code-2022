import sys

input_file = sys.argv[1]


def part_one():
    sub_count = 0
    with open(input_file, "r") as f:
        lines = f.read().splitlines()
        for line in lines:
            section = line.split(",")

            s1 = [int(x) for x in section[0].split("-")]
            s2 = [int(x) for x in section[1].split("-")]

            if (s1[0] <= s2[0]) and (s2[1] <= s1[1]) or (s2[0] <= s1[0]) and (s1[1] <= s2[1]):
                sub_count += 1

        print(sub_count)


def part_two():
    with open(input_file, "r") as f:
        lines = f.read().splitlines()
        sub_count = 0
        for line in lines:
            section = line.split(",")

            s1 = [int(x) for x in section[0].split("-")]
            s2 = [int(x) for x in section[1].split("-")]

            if not (s1[1] < s2[0] or s2[1] < s1[0]):
                sub_count += 1

        print(sub_count)


part_one()
part_two()
