seq = []
xInc = 3
yInc = 1
msgTest = "Trying position (%d,%d)..."
msgPass = "space"
msgFail = "tree"
msgResult = "You hit %d trees."

testseq = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#"
]


def readInput(file, list):
    file = open(file, "r")
    for line in file.readlines():
        seq.append(line.rstrip())


def checkForTrees(seq, xInc, yInc):
    x = 0
    y = 0
    trees = 0
    for y in range(len(seq)):
        x += xInc
        y += yInc
        if x >= len(seq[0]):
            x = x - len(seq[0])
        if y >= len(seq):
            return trees
        print(msgTest % (x, y))
        if seq[y][x] == "#":
            print(msgFail)
            trees += 1
        else:
            print(msgPass)
    return None


readInput("day3-input.txt", seq)
trees = checkForTrees(seq, xInc, yInc)
print(msgResult % trees)
