import sys

input_file = sys.argv[1]


def part_one():
    sub_count = 0
    with open(input_file, "r") as f:
        lines = f.read().splitlines()
        for line in lines:
            section = line.split(",")

            section1 = section[0].split("-")
            section2 = section[1].split("-")

            # TODO: Work on solution later... Sleepy ZZzzzZZ

            # section1 is subgroup
            if (section1[0] >= section2[0]) and (section1[1] <= section2[1]):
                sub_count += 1
                print(section, "2 is subgroup")

            # section2 is subgroup
            if (section1[0] <= section2[0]) and (section1[1] >= section2[1]):
                sub_count += 1
                print(section, "1 is subgroup")

        print(sub_count)


def part_two():
    pass


part_one()
