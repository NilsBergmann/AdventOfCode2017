def solve1(lines):
    count = 0 
    for line in lines:
        if(len(line) == len(set(line))):
            count += 1
    print("Solve 1:", count)     

import itertools
def solve2(lines):
    count = 0 
    for line in lines:
        isValid = True
        for wordA, wordB in itertools.combinations(line, 2):
            if sorted(wordA) == sorted(wordB):
                isValid = False
        if isValid:
            count += 1
    print("Solve 1:", count)

_input = open("Day4/Input.txt", "r")
lines = []
for line in _input: 
    lines.append(line.split())
solve1(lines)
solve2(lines)