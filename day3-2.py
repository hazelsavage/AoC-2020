seq = []
msgTest = "Trying position (%d,%d)..."
msgPass = "space"
msgFail = "tree"
msgResult = "For the %s slope you hit %d trees.\n"
msgMult = "The puzzle answer is %d."


slopeA = [1, 1]
slopeB = [3, 1]
slopeC = [5, 1]
slopeD = [7, 1]
slopeE = [1, 2]
slopes = [slopeA, slopeB, slopeC, slopeD, slopeE]

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
    while y < len(seq):
        x += xInc
        y += yInc
        if x >= len(seq[0]):
            x = x - len(seq[0])
        if y >= len(seq):
            return trees
        print(msgTest % (x, y), end=" ")
        if seq[y][x] == "#":
            print(msgFail)
            trees += 1
        else:
            print(msgPass)
    return None


def checkManyTrees(slopes, seq):
    manyTrees = []
    for slope in slopes:
        xInc = slope[0]
        yInc = slope[1]
        trees = checkForTrees(seq, xInc, yInc)
        print(msgResult % (slope, trees))
        manyTrees.append(trees)
    return manyTrees


def multiply(manyTrees):
    mult = 1
    for trees in manyTrees:
        mult = mult * trees
    return mult


readInput("day3-input.txt", seq)
manyTrees = checkManyTrees(slopes, seq)
print(manyTrees)
mult = multiply(manyTrees)
print(msgMult % mult)
