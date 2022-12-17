import sys

# part 1

input_file = sys.argv[1]

tie_states = {
    "rock": ["A", "X"],
    "paper": ["B", "Y"],
    "scissors": ["C", "Z"]
}

game_result = {
    "loss": 0,
    "draw": 3,
    "win": 6
}

with open(input_file, "r") as f:
    data = f.read().split("\n")

p1_score = 0
p2_score = 0


def find_score_part_one():
    for line in data:
        p1 = line[0]
        p2 = line[2]

        if p1 == "A":
            p1_score += 1
            if p2 == "X":
                p2_score += 1
                # tie
                p1_score += 3
                p2_score += 3
            if p2 == "Y":
                p2_score += 2
                # p2 win
                p2_score += 6
            if p2 == "Z":
                p2_score += 3
                # p2 loss
                p1_score += 6
        if p1 == "B":
            p1_score += 2
            if p2 == "X":
                p2_score += 1
                # loss
                p1_score += 6
            if p2 == "Y":
                p2_score += 2
                # tie
                p1_score += 3
                p2_score += 3
            if p2 == "Z":
                p2_score += 3
                # win
                p2_score += 6
        if p1 == "C":
            p1_score += 3
            if p2 == "X":
                p2_score += 1
                p2_score += 6  # win
            if p2 == "Y":
                p2_score += 2
                p1_score += 6  # loss
            if p2 == "Z":
                p2_score += 3
                # tie
                p1_score += 3
                p2_score += 3

    print("p1:", p1_score)
    print("p2:", p2_score)


# part 2

def find_score_part_two():
    p2_score = 0
    for line in data:
        p1 = line[0]
        p2 = line[2]

        if p1 == "A":
            if p2 == "X":
                # you lose (scissors)
                p2_score += 3
                pass
            if p2 == "Y":
                # you draw (rock)
                p2_score += 1
                p2_score += 3
                pass
            if p2 == "Z":
                # you win (paper)
                p2_score += 2
                p2_score += 6
                pass
        if p1 == "B":
            if p2 == "X":
                # you lose (rock)
                p2_score += 1
            if p2 == "Y":
                # you draw (paper)
                p2_score += 2
                p2_score += 3
            if p2 == "Z":
                # you win (scissors)
                p2_score += 3
                p2_score += 6
        if p1 == "C":
            if p2 == "X":
                # you lose (paper)
                p2_score += 2
            if p2 == "Y":
                # you draw (scissors)
                p2_score += 3
                p2_score += 3
            if p2 == "Z":
                # you win (rock)
                p2_score += 1
                p2_score += 6

    print("p2:", p2_score)


find_score_part_two()
