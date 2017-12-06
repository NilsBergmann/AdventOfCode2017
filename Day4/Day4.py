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
        for wordA, wordB in itertools.product(line, line):
            if sorted(wordA) == sorted(WordB):

_input = open("Day4/Input.txt", "r")
lines = []
for line in _input: 
    lines.append(line.split())
solve1(lines)