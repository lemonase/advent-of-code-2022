import sys

input_file = sys.argv[1]

with open(input_file, "r") as f:
    data = f.read()

elves = []

arr = data.split("\n\n")
for i, e in enumerate(arr):
    e = [int(x) for x in e.split("\n")]
    elves.append(sum(e))


print(sorted(elves))
